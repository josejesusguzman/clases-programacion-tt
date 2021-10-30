const pokedex = document.getElementById('pokedex');

const getPokemon = () => {
    const promesas = [];
    for (let i = 1; i <= 151; i++) {
        const url = `https://pokeapi.co/api/v2/pokemon/${i}`
        promesas.push(fetch(url).then(res => res.json()));
    }
    
    Promise.all(promesas).then(resultados => {
        const pokemons = resultados.map((result) => ({
            name : result.name,
            id : result.id,
            img : result.sprites.front_default,
            type : result.types.map(type => type.type.name)
        }));

        showPokemon(pokemons);

    });
}

const showPokemon = (pokemon) => {
    console.log(pokemon);
    const pokemonHTML = 
        pokemon.map((poke)=> 
            `<li class="card">
                <img class="card-img" src="${poke.img}"/>
                <h2 class="card-subtitle">${poke.name}</h2>
                <p class="card-text">${poke.type}</p>
            </li>`
        ).join('');
    pokedex.innerHTML = pokemonHTML;
}

getPokemon();
