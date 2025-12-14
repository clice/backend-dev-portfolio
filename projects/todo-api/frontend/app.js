const API = "http://127.0.0.1:8000";

function register() {
    fetch(API + "/users", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    }).then(() => alert("Usuário criado"));
}

function login() {
    fetch(API + "/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            username: username.value,
            password: password.value
        })
    })
    .then(r => r.json())
    .then(data => {
        localStorage.setItem("token", data.access_token);
        window.location = "tasks.html";
    });
}

function loadTasks() {
    fetch(API + "/tasks", {
        headers: {
            "Authorization": "Bearer " + localStorage.getItem("token")
        }
    })
    .then(r => r.json())
    .then(tasks => {
        const ul = document.getElementById("tasks");
        ul.innerHTML = "";
        tasks.forEach(t => {
            ul.innerHTML += `<li>${t.title}</li>`;
        });
    });
}

function createTask() {
    fetch(API + "/tasks", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + localStorage.getItem("token")
        },
        body: JSON.stringify({title: title.value})
    }).then(loadTasks);
}

if (window.location.pathname.includes("tasks")) {
    loadTasks();
}
