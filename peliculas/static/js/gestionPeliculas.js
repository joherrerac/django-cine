(function(){
    const btnEliminacion = document.querySelectorAll(".btnEliminacion");

    btnEliminacion.forEach(btn=>{
    btn.addEventListener('click', (e) => {
        const confirmacion = confirm('¿seguro quieres eliminar esta pelicula?');
        if(!confirmacion){
            e.preventDefault();
        }
    });
    });
    })();