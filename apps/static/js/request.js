// XHR requests
// export function getData(endpoint, callback) {
//   const request = new XMLHttpRequest();
//   request.onreadystatechange = () => {
//     if (request.readyState === 4) {
//       callback(request.response);
//     }
//   };
//   request.open("GET", endpoint);
//   request.send();
// }

// export function sendForm(form, action, endpoint, callback) {
//   const formData = new FormData(form);
//   const dataJSON = JSON.stringify(Object.fromEntries(formData));

//   const request = new XMLHttpRequest();
//   request.onreadystatechange = () => {
//     if (request.readyState === 4) {
//       callback(request.response, form);
//     }
//   };
//   request.open(action, endpoint);
//   request.setRequestHeader("Content-Type", "application/json");
//   request.send(dataJSON);
// }

// Fetch requests
export function getData(endpoint, callback) {
  fetch(endpoint)
    .then(response => response.text())
    .then(data => callback(data))
    .catch(error => console.error('Error:', error));
}

export function sendForm(form, action, endpoint, callback) {
  const formData = new FormData(form);
  const dataJSON = JSON.stringify(Object.fromEntries(formData));

  fetch(endpoint, {
    method: action,
    headers: {
      'Content-Type': 'application/json'
    },
    body: dataJSON
  })
  .then(response => response.text())
  .then(data => callback(data, form))
  .catch(error => console.error('Error:', error));
}