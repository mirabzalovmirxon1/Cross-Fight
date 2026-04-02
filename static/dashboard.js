document.addEventListener('DOMContentLoaded', () => {
    // Mock progress values
    let missionsPercent = 80; // 8/10
    let xpPercent = 45; // 450 XP / 1000
    let winsPercent = 30; // 3/10

    document.getElementById('missionsProgress').style.width = missionsPercent + '%';
    document.getElementById('xpProgress').style.width = xpPercent + '%';
    document.getElementById('winsProgress').style.width = winsPercent + '%';
});

function navigate(page){
    alert(`Navigate to ${page} (to be implemented)`);
}