let carre = false;
let rouge = false;

document.querySelector('.bouton1').addEventListener('click', () => {
    document.querySelectorAll('td.aspect').forEach(td => {
        const n = parseInt(td.textContent);
        td.textContent = carre ? Math.round(Math.sqrt(n)) : n * n;
    });
    carre = !carre;
});

function multiples() {
    if (!rouge) {
        const choix = parseInt(prompt("Entrez un nombre :"));
        document.querySelectorAll('td.aspect').forEach(td => {
            const n = parseInt(td.textContent);
            if (n % choix === 0) {
                td.className = 'aspect rouge';
            }
        });
    } else {
        document.querySelectorAll('td.aspect').forEach(td => {
            td.className = 'aspect';
        });
    }
    rouge = !rouge;
}

document.querySelector('.bouton2').addEventListener('click', multiples);
