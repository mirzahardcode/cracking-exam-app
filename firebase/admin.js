// Firebase Admin Panel Logic
const FIREBASE_URL = "https://ujianxthax-default-rtdb.asia-southeast1.firebasedatabase.app/";

async function loadUsers() {
    const res = await fetch(FIREBASE_URL + "users.json");
    const data = await res.json();
    renderTable(data);
}

function renderTable(data) {
    const tbody = document.getElementById('userTableBody');
    let html = '';
    for (const [username, user] of Object.entries(data)) {
        html += `
            <tr>
                <td>${username}</td>
                <td>${user.hwid || '-'}</td>
                <td>${user.banned ? 'Banned' : 'Active'}</td>
            </tr>
        `;
    }
    tbody.innerHTML = html;
}

// Export for ES6 modules
export { loadUsers, renderTable };
