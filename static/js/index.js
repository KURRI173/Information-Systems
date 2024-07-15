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
        console.log("Added to favourites:", favourite);
    } else {
        console.log("Item is already in favourites");
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

        favouriteContainer.appendChild(div);
    });
}
});