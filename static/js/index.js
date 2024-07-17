let favourites = [];

function AddFavourites(element) {
    const second = element.closest('.sectiondestination');
    const image = second.getAttribute('data-image');
    const title = second.getAttribute('data-title');
    const subtitle = second.getAttribute('data-subtitle');
    const city = second.getAttribute('data-city');
    const price = second.getAttribute('data-price');
    
    let favourite = { "image": image, "title": title, "subtitle": subtitle, "city": city, "price": price };

    // Retrieve existing favourites from sessionStorage
    let storedFavourites = sessionStorage.getItem('favourites');
    if (storedFavourites) {
        favourites = JSON.parse(storedFavourites);
    }

    // Check if the favourite item is already in the favourites array
    const exists = favourites.find(fav => JSON.stringify(fav) === JSON.stringify(favourite));

    if (!exists) {
        favourites.push(favourite);
        alert("Added to favourites");
    } else {
        alert("Item is already in favourites");
    }

    // Update sessionStorage with the new favourites array
    sessionStorage.setItem('favourites', JSON.stringify(favourites));

    // Send favourites to server
    // fetch('/favourites', {
    //     headers: {
    //         'Content-Type': 'application/json'
    //     },
    //     method: 'POST',
    //     body: JSON.stringify({ favourites })
    // })
    // .then(response => response.json())
    // .then(data => {
    //     console.log("Result:", data);
    // })
    // .catch(error => {
    //     console.log("Error:", error);
    // });
}

document.addEventListener('DOMContentLoaded', () => {
    if(window.location.pathname=="/favourites")
    {

    const favouriteContainer = document.querySelector('.favoritesubsection');

    const items = JSON.parse(sessionStorage.getItem('favourites')) || [];
    items.forEach(item => {
        const div = document.createElement('div');
        div.classList.add('favouritetour');

        const img = document.createElement('img');
        img.src = item.image;
        img.style.width="100px";
        img.style.height="100px"
        div.appendChild(img);

        const title = document.createElement('h4');
        title.textContent = item.title;
        div.appendChild(title);

        const subtitle = document.createElement('h4');
        subtitle.textContent = item.subtitle;
        div.appendChild(subtitle);

        const city = document.createElement('h4');
        city.textContent = item.city;
        div.appendChild(city);

        const price = document.createElement('h4');
        price.textContent = item.price;
        div.appendChild(price);

        const remove = document.createElement('button');
        remove.textContent = "Remove";
        div.appendChild(remove);
        remove.addEventListener('click',()=>clickremove(item))

        favouriteContainer.appendChild(div);
    });
}
});
function clickremove(item)
{
    const items = JSON.parse(sessionStorage.getItem('favourites')) || [];
    const index = items.findIndex(fav => JSON.stringify(fav) === JSON.stringify(item));

    if (index === -1) {
        console.log("Item not exists!");
    } else {
        items.splice(index, 1);
        sessionStorage.setItem('favourites', JSON.stringify(items));
        console.log("Item removed");
        window.location.reload();
    }
}
const afterSearchContainer=document.querySelector('.aftersearch');

const beforeSearchContainer=document.querySelector('.beforesearch');

const search=document.querySelector('#search');

const searchB=document.querySelector('#searchButton');
let searchValues=""

search.addEventListener('input',(e)=>{searchValues=e.target.value;console.log(searchValues)});


searchB.addEventListener('click',(e)=>{
    if(searchValues==null ||searchValues=="")
    {
        return;
    }
    afterSearchContainer.style.display="block";
    beforeSearchContainer.style.display="none";
    fetch(`/search/${searchValues}`, { method: 'GET' })
    .then(res => {
        if (!res.ok) {
            throw new Error('Network response was not ok');
        }
        return res.json();
    })
    .then(products => {
        const container = afterSearchContainer.querySelector('.hotelpanel');
        container.innerHTML = ''; // Clear previous search results
        products.forEach(product => {
            const productDiv = document.createElement('div');
            productDiv.className = 'hotelsubpanel';
            productDiv.innerHTML = `
                <div class="hotelimage">
                    <img src="${product.imgpath}" alt="${product.name}"/>
                </div>
                <div class="textarea">
                    <h2>${product.name}</h2>
                    <h3>${product.price}</h3>
                    <button onclick="window.location.href='/destination'">Check Prices</button>
                </div>
            `;
            container.append(productDiv);
        });
    })
    .catch(e => console.log('Error:', e));
});

