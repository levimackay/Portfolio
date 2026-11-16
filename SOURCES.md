# Sources

Every figure on levimackay.com: the claim, the command that produced it, who ran it and when.
Commands run from the root of the project's own repository.

## izvor: home page line

- Claim: "41 golden programs have to produce byte for byte the same output from the interpreter and the compiled binary."
- Source: the counts under "izvor: Golden programs"
- Supplied by: Levi Mackay
- Date: 2026-11-14

## izvor: Golden programs

- Claim: Golden programs: 41
- Source: counted in the izvor repository with `git ls-tree -r --name-only origin/main | grep '^tests/golden/.*\.iz$' | wc -l`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/izvor/tree/main/tests/golden

## izvor: Fuzz inputs per CI run

- Claim: Fuzz inputs per CI run: 20,000
- Source: counted in the izvor repository with `git show origin/main:tests/fuzz.c | grep -n ITERATIONS`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/izvor/blob/main/tests/fuzz.c

## izvor: Lines of C

- Claim: Lines of C: 2,822
- Source: counted in the izvor repository with `git ls-tree -r --name-only origin/main -- src | while read f; do git show origin/main:$f; done | wc -l`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/izvor/tree/main/src

## lydia: home page line

- Claim: "Open source with 38 stars, and pull requests merged from developers who found it on their own."
- Source: the counts under "lydia: GitHub stars", "lydia: Outside pull requests merged"
- Supplied by: Levi Mackay
- Date: 2026-11-14

## lydia: GitHub stars

- Claim: GitHub stars: 38
- Source: counted in the Lydia repository with `gh api repos/levimackay/lydia-cli --jq '{stars:.stargazers_count,forks:.forks_count,pushed:.pushed_at}'`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/lydia-cli

## lydia: GitHub forks

- Claim: GitHub forks: 8
- Source: counted in the Lydia repository with `gh api repos/levimackay/lydia-cli --jq '{stars:.stargazers_count,forks:.forks_count,pushed:.pushed_at}'`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/lydia-cli

## lydia: Outside pull requests merged

- Claim: Outside pull requests merged: 2
- Source: counted in the Lydia repository with `gh pr list --repo levimackay/lydia-cli --state merged --limit 50 --json number,title,author,mergedAt`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/lydia-cli/pulls?q=is%3Apr+is%3Amerged

## lydia: Lines of Python in src and server

- Claim: Lines of Python in src and server: 8,573
- Source: counted in the Lydia repository with `git ls-tree -r --name-only origin/main | grep -E '^(src|server)/.*\.py$', then git show origin/main:<file> | wc -l for each of the 85 files, summed`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/lydia-cli

## lydia: Tests

- Claim: Tests: 413
- Source: counted in the Lydia repository with `git grep -c -E '^[[:space:]]*(async )?def test_' origin/main -- '*.py', summed for the 53 files under tests/`
- Supplied by: Levi Mackay
- Date: 2026-11-14
- Check it: https://github.com/levimackay/lydia-cli/tree/main/tests

## proven-blue: home page line

- Claim: "57 database migrations, 110 row level security policies and 446 backend tests."
- Source: the counts under "proven-blue: Numbered SQL migrations", "proven-blue: Row level security policies", "proven-blue: Backend tests"
- Supplied by: Levi Mackay
- Date: 2026-11-14

## proven-blue: Numbered SQL migrations

- Claim: Numbered SQL migrations: 57
- Source: counted in the Proven Blue repository with `git ls-tree -r --name-only origin/main -- backend/supabase | grep -cE '^backend/supabase/[0-9]{3}_[^/]+\.sql$'`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## proven-blue: Row level security policies

- Claim: Row level security policies: 110
- Source: counted in the Proven Blue repository with `git grep -i -c -E 'create policy' origin/main -- '*.sql', summed`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## proven-blue: Database test files

- Claim: Database test files: 27
- Source: counted in the Proven Blue repository with `git ls-tree -r --name-only origin/main -- backend/supabase/tests | wc -l`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## proven-blue: Backend tests

- Claim: Backend tests: 446
- Source: counted in the Proven Blue repository with `git grep -c -E "^[[:space:]]*(test|it)\(" origin/main -- 'backend/*.test.ts', summed for the 28 files`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## proven-blue: My commits, of all commits

- Claim: My commits, of all commits: 371 of 409
- Source: counted in the Proven Blue repository with `git shortlog -sn origin/main`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## tieout: home page line

- Claim: "Early: so far it has only been run on sample files."
- Source: my own statement of where the project stands, with no count behind it
- Supplied by: Levi Mackay
- Date: 2026-11-11

## tieout: Tests

- Claim: Tests: 116
- Source: counted in the tieout repository with `git grep -c -E "^[[:space:]]*(async )?def test_" origin/main -- tests, summed for the 9 test files`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## tieout: Lines of Python, tests included

- Claim: Lines of Python, tests included: 5,338
- Source: counted in the tieout repository with `git grep -I -c '' origin/main -- '*.py', summed for the 23 files`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## tieout: Third party runtime dependencies

- Claim: Third party runtime dependencies: 0
- Source: counted in the tieout repository with `git ls-tree -r --name-only origin/main | grep -E 'pyproject|requirements|setup\.' (no output)`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## mckay-jewelers: home page line

- Claim: "Live on the store's own domain."
- Source: the site itself, at https://mckayjewelersmagicvalley.com
- Supplied by: Levi Mackay
- Date: 2026-11-11

## mckay-jewelers: Commits

- Claim: Commits: 35
- Source: counted in the McKay Jewelers repository with `git rev-list --count origin/main`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## mckay-jewelers: Lines of JSX

- Claim: Lines of JSX: 1,706
- Source: counted in the McKay Jewelers repository with `git grep -I -c '' origin/main -- '*.jsx', summed for the 35 files`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## mckay-jewelers: Tests

- Claim: Tests: 13
- Source: counted in the McKay Jewelers repository with `git grep -c -E "^[[:space:]]*(test|it)\(" origin/main -- tests, summed for the 2 files`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## dev-dock: tool count

- Claim: Twenty-two developer tools in one static React app.
- Source: counted in the Dev Dock repository with `git show origin/main:src/tools/registry.ts | awk '/export const TOOLS/{f=1} f && /^    id: /{n++} END{print n}'`
- Supplied by: Levi Mackay
- Date: 2026-11-14

## dictionary: page count

- Claim: A 301 page Serbo-Croatian dictionary.
- Source: counted in the dictionary repository with `pdfinfo build/Srpsko-Hrvatski.pdf | grep Pages`, on the PDF the build writes. Line 5 of the README gives the same figure
- Supplied by: Levi Mackay
- Date: 2026-11-14

## mckay-jewelers: first paying client

- Claim: My first paying client, a jewelry store in Twin Falls.
- Source: my resume of 2026-11-04
- Supplied by: Levi Mackay
- Date: 2026-11-04

## about: school and work

- Claim: A computer science student at BYU-Idaho, graduating in December 2027. A teaching assistant for the programming courses and a fellow in Sandbox.
- Source: my resume of 2026-11-04
- Supplied by: Levi Mackay
- Date: 2026-11-04

## about: languages

- Claim: Two years in Bosnia, Croatia and Serbia, and all three languages.
- Source: my own account. My resume of 2026-11-04 lists Serbian, Croatian and Bosnian, and the two years of field notes behind the dictionary
- Supplied by: Levi Mackay
- Date: 2026-11-04
