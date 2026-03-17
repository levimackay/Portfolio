function isCardNumberValid(number) {
  return number === '1234123412341234';
}

function displayError(msg) {
  document.querySelector('.errorMsg').innerHTML = msg;
}

function submitHandler(event) {
  event.preventDefault();
  let errorMsg = '';
  displayError('');

  const cardNumber = this.cardNumber.value;
  const expMonth = parseInt(this.expMonth.value);
  const expYear = parseInt(this.expYear.value);
  const now = new Date();
  const currentYear = now.getFullYear();
  const currentMonth = now.getMonth() + 1;

  if (isNaN(cardNumber)) {
    errorMsg += 'Card number must be numeric.<br>';
  } else if (!isCardNumberValid(cardNumber)) {
    errorMsg += 'Invalid card number.<br>';
  }

  if (expYear < currentYear || (expYear === currentYear && expMonth < currentMonth)) {
    errorMsg += 'Expiration date must be in the future.<br>';
  }

  if (errorMsg !== '') {
    displayError(errorMsg);
    return false;
  }

  alert('Form submitted successfully!');
  return true;
}

document.querySelector('#credit-card').addEventListener('submit', submitHandler);
