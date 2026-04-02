// PAGE SWITCH
function showPage(page) {
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    document.getElementById(page).classList.add('active');
}

// LOGIN (backend bilan)
function login() {
    fetch("/api/account/login/", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        })
    })
    .then(res => res.json())
    .then(data => {
        localStorage.setItem("access", data.access);
        alert("Login success ⚡");
        showPage('dashboard');
    });
}

// FIGHT ANSWER
function answer() {
    alert("Correct ⚡ +10 XP");
}