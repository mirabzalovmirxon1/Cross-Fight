const loginForm = document.getElementById('loginForm');

loginForm.addEventListener('submit', function(e){
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const role = document.getElementById('role').value;

    // Mock fetch to backend
    fetch('/api/accounts/login/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password, role })
    })
    .then(res => res.json())
    .then(data => {
        if(data.access){
            alert(`Login successful! Welcome ${role}`);
            window.location.href = 'dashboard.html';
        } else {
            alert('Login failed');
        }
    })
    .catch(err => console.log(err));
});

function switchForm(){
    alert('Switch to register form (future implementation)');
}