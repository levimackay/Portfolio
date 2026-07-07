// ============================================================
// Hero 3D scene — a sphere of shards that assembles on load
// and explodes toward the camera as you scroll.
// Debug: append ?p=0.5 to the URL to freeze scroll progress.
// ============================================================

(function () {
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canvas = document.getElementById('scene');
  if (!canvas || !window.THREE || reduceMotion) {
    if (canvas) canvas.remove();
    return;
  }

  var renderer;
  try {
    renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
  } catch (e) {
    canvas.remove();
    return;
  }

  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.setSize(window.innerWidth, window.innerHeight);

  var scene = new THREE.Scene();
  var camera = new THREE.PerspectiveCamera(50, window.innerWidth / window.innerHeight, 0.1, 100);
  camera.position.z = 9;

  // ---------- Lights ----------
  scene.add(new THREE.AmbientLight(0x8899aa, 0.45));

  var key = new THREE.DirectionalLight(0xffffff, 0.9);
  key.position.set(5, 8, 6);
  scene.add(key);

  var blue = new THREE.PointLight(0x2997ff, 1.6, 30);
  blue.position.set(-6, -3, 5);
  scene.add(blue);

  var violet = new THREE.PointLight(0x8c5cff, 1.3, 30);
  violet.position.set(6, 4, -4);
  scene.add(violet);

  // ---------- Shards ----------
  var isMobile = window.innerWidth < 700;
  var COUNT = isMobile ? 280 : 520;
  var RADIUS = isMobile ? 2.1 : 2.6;

  var group = new THREE.Group();
  scene.add(group);

  var shardGeo = new THREE.TetrahedronGeometry(0.16);
  var shardMat = new THREE.MeshStandardMaterial({
    metalness: 0.55,
    roughness: 0.3,
    transparent: true,
  });
  var shards = new THREE.InstancedMesh(shardGeo, shardMat, COUNT);
  group.add(shards);

  var palette = [
    new THREE.Color(0xd8dde6), // slate white
    new THREE.Color(0xd8dde6),
    new THREE.Color(0x9fb4cc),
    new THREE.Color(0x2997ff), // accent blue
    new THREE.Color(0x2997ff),
    new THREE.Color(0x8c5cff), // violet
  ];

  var base = [];      // resting position on the sphere shell
  var dir = [];       // explosion direction
  var dist = [];      // explosion distance
  var axis = [];      // tumble axis
  var speed = [];     // tumble speed
  var scale = [];     // per-shard size
  var phase = [];     // breathing phase

  var v = new THREE.Vector3();
  for (var i = 0; i < COUNT; i++) {
    // Even-ish distribution on a sphere via normalized gaussians
    v.set(gauss(), gauss(), gauss()).normalize();
    var r = RADIUS * (0.94 + Math.random() * 0.14);
    base.push(v.clone().multiplyScalar(r));

    // Explode mostly outward with a tangential kick for swirl
    var d = v.clone();
    var tangent = new THREE.Vector3(gauss(), gauss(), gauss()).cross(v).normalize();
    d.addScaledVector(tangent, 0.55 * Math.random()).normalize();
    dir.push(d);
    dist.push(4 + Math.random() * 9);

    axis.push(new THREE.Vector3(gauss(), gauss(), gauss()).normalize());
    speed.push(0.3 + Math.random() * 1.4);
    scale.push(0.55 + Math.random() * 1.1);
    phase.push(Math.random() * Math.PI * 2);

    shards.setColorAt(i, palette[Math.floor(Math.random() * palette.length)]);
  }
  if (shards.instanceColor) shards.instanceColor.needsUpdate = true;

  function gauss() {
    return (Math.random() + Math.random() + Math.random()) - 1.5;
  }

  // ---------- Glowing core ----------
  var core = new THREE.Mesh(
    new THREE.IcosahedronGeometry(0.55, 2),
    new THREE.MeshBasicMaterial({ color: 0x2997ff, transparent: true, opacity: 0.9 })
  );
  group.add(core);

  var coreGlow = new THREE.PointLight(0x2997ff, 2.2, 12);
  group.add(coreGlow);

  var wire = new THREE.Mesh(
    new THREE.IcosahedronGeometry(RADIUS * 1.02, 1),
    new THREE.MeshBasicMaterial({ color: 0x2997ff, wireframe: true, transparent: true, opacity: 0.07 })
  );
  group.add(wire);

  // ---------- Animation state ----------
  var dummy = new THREE.Object3D();
  var quat = new THREE.Quaternion();
  var introStart = performance.now();
  var INTRO_MS = 2000;
  var mouseX = 0, mouseY = 0;
  var rotX = 0, rotY = 0;

  var forcedP = parseFloat(new URLSearchParams(location.search).get('p'));

  // Fully stop the render loop (not just the per-frame work) once the hero
  // has scrolled out of view, and resume it if the user scrolls back up.
  // A `setAnimationLoop` callback that merely early-returns still gets
  // invoked every frame for as long as the page is open, which keeps the
  // WebGL context "hot" and adds up over a long scroll session.
  var looping = true;
  function syncLoop() {
    if (!isNaN(forcedP)) return;
    var p = window.scrollY / (window.innerHeight * 1.15);
    var shouldRun = p < 1.18;
    if (shouldRun && !looping) {
      looping = true;
      canvas.style.visibility = 'visible';
      renderer.setAnimationLoop(tick);
    } else if (!shouldRun && looping) {
      looping = false;
      canvas.style.visibility = 'hidden';
      renderer.setAnimationLoop(null);
    }
  }
  window.addEventListener('scroll', syncLoop, { passive: true });

  window.addEventListener('mousemove', function (e) {
    mouseX = (e.clientX / window.innerWidth) * 2 - 1;
    mouseY = (e.clientY / window.innerHeight) * 2 - 1;
  });

  window.addEventListener('resize', function () {
    camera.aspect = window.innerWidth / window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth, window.innerHeight);
  });

  // Let the terminal's `explode` command replay the assembly intro
  window.__replayIntro = function () {
    introStart = performance.now();
  };

  function easeOutCubic(x) { return 1 - Math.pow(1 - x, 3); }
  function smoothstep(a, b, x) {
    var t = Math.min(1, Math.max(0, (x - a) / (b - a)));
    return t * t * (3 - 2 * t);
  }

  function tick(now) {
    var t = now * 0.001;

    // Scroll progress: 0 at top → 1 once the hero has scrolled past
    var p = window.scrollY / (window.innerHeight * 1.15);
    if (!isNaN(forcedP)) p = forcedP;
    p = Math.min(1.2, Math.max(0, p));

    // Intro: fly in from exploded. Scroll: explode again.
    var intro = 1 - easeOutCubic(Math.min(1, (now - introStart) / INTRO_MS));
    if (!isNaN(forcedP)) intro = 0;
    var e = Math.max(intro, easeOutCubic(Math.min(1, p)));

    // Whole-group motion: slow spin + mouse parallax
    rotY += ((t * 0.07 + mouseX * 0.3) - rotY) * 0.04;
    rotX += ((Math.sin(t * 0.11) * 0.06 + mouseY * 0.18) - rotX) * 0.04;
    group.rotation.y = rotY;
    group.rotation.x = rotX;

    // Camera pushes forward as shards fly outward → fly-through
    camera.position.z = 9 - easeOutCubic(Math.min(1, p)) * 3.6;
    camera.position.y = -p * 1.2;

    var breathe = 1 - e;
    for (var i = 0; i < COUNT; i++) {
      var b = base[i];
      var puff = Math.sin(t * 0.9 + phase[i]) * 0.06 * breathe;
      var out = e * dist[i] + puff;

      dummy.position.set(
        b.x + dir[i].x * out,
        b.y + dir[i].y * out,
        b.z + dir[i].z * out
      );
      quat.setFromAxisAngle(axis[i], t * speed[i] + e * 5 * speed[i]);
      dummy.quaternion.copy(quat);
      var s = scale[i] * (1 - 0.35 * e);
      dummy.scale.set(s, s, s);
      dummy.updateMatrix();
      shards.setMatrixAt(i, dummy.matrix);
    }
    shards.instanceMatrix.needsUpdate = true;

    // Fade everything late in the scroll
    var fade = 1 - smoothstep(0.55, 1.05, p);
    shardMat.opacity = fade;

    var corePulse = 1 + Math.sin(t * 1.6) * 0.06;
    var coreScale = corePulse * (1 - smoothstep(0, 0.6, e) * 0.85);
    core.scale.set(coreScale, coreScale, coreScale);
    core.material.opacity = 0.9 * fade * (1 - e * 0.6);
    coreGlow.intensity = 2.2 * fade;

    wire.material.opacity = 0.07 * fade * (1 - e);
    var ws = 1 + e * 2.5;
    wire.scale.set(ws, ws, ws);

    renderer.render(scene, camera);
  }

  renderer.setAnimationLoop(tick);
  syncLoop();
})();
