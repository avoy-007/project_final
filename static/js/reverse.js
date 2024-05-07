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
    
    fetch('/reverse', {
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
            // console.log(document.getElementsByClassName('box')[0])
            box0 = document.getElementsByClassName('box')[0].innerHTML = `${data.cement}`
            box1 = document.getElementsByClassName('box')[1].innerHTML = `${data.water}`
            box2 = document.getElementsByClassName('box')[2].innerHTML = `${data.fine_aggregate}`
            box3 = document.getElementsByClassName('box')[3].innerHTML = `${data.coarse_aggregate}`
            // alert(`${data.predicted_strength}`);
        }).catch(error => {
            console.error('Error:', error);
        });
});