const target = document.getElementById("target")

const first = documentcreateElement("li");
first.textcontent = "first item"
target.appendChild(first);

const second = document.createElement("li");
second.textContent = "Second item"
second.classList.add("my item");
target.appendChild(second);

const third = document.createElement("li");
third.textContent = "third item"
target.appendChild(third);