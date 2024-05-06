const loadingSection = document.getElementById('loading');
const contentSection= document.getElementById('content');

document.getElementById('predictionForm').addEventListener('submit', function (event) {
    event.preventDefault();
    loadingSection.style.display = 'flex';
    contentSection.style.display = 'none';
    let form = {};
    const inputArray = document.getElementsByTagName('input');
    console.log(inputArray);
    for (let i = 0; i < inputArray.length; i++) {
        const element = inputArray[i];
        const name = element.getAttribute('name');    
        form[name] = element.value;    
    }

    console.log({form});
    
    fetch('/slump', {
        method: 'POST',
        body: JSON.stringify(form),
        headers: {
            'Content-Type': 'application/json', // Setting content type to JSON
        },
    }).then(response => response.json())
        .then(data => {
            console.log(data);
            loadingSection.style.display = 'none';
            contentSection.style.display = 'block';
            box = document.getElementById('box').innerHTML = `${data.predicted_strength}`
            // alert(`${data.predicted_strength}`);
        }).catch(error => {
            console.error('Error:', error);
        });
});