// Example mock data, in real project fetch from backend
const leaderboardData = [
    {rank: 1, name: 'Alice', level: 12, points: 450, current: false},
    {rank: 2, name: 'Bob', level: 11, points: 420, current: false},
    {rank: 3, name: 'You', level: 10, points: 400, current: true},
    {rank: 4, name: 'Charlie', level: 9, points: 380, current: false},
    {rank: 5, name: 'Diana', level: 8, points: 350, current: false},
];

function renderLeaderboard(data){
    const tbody = document.getElementById('leaderboard-body');
    tbody.innerHTML = '';

    data.forEach(player => {
        const tr = document.createElement('tr');
        if(player.current) tr.classList.add('current-user');

        tr.innerHTML = `
            <td>${player.rank} ${getMedal(player.rank)}</td>
            <td>${player.name}</td>
            <td>${player.level}</td>
            <td>${player.points}</td>
        `;

        tbody.appendChild(tr);
    });
}

function getMedal(rank){
    if(rank === 1) return '🥇';
    if(rank === 2) return '🥈';
    if(rank === 3) return '🥉';
    return '';
}

// Filter buttons (just mock for now)
function filterLeaderboard(type){
    alert('Filter: ' + type);
    // TODO: Fetch filtered data from backend
}

// Initial render
renderLeaderboard(leaderboardData);