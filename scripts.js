const itemList = document.getElementById("itemList");
const addButton = document.getElementById("addButton");
const removeButton = document.getElementById("removeButton");
const modifyButton = document.getElementById("modifyButton");

addButton.addEventListener("click", () => {
  const newItem = prompt("Enter a new item:");
  if (newItem) {
    const li = document.createElement("li");
    li.textContent = newItem;
    itemList.appendChild(li);
  }
});

removeButton.addEventListener("click", () => {
  if (itemList.children.length > 0) {
    itemList.removeChild(itemList.lastChild);
  }
});

modifyButton.addEventListener("click", () => {
  if (itemList.children.length > 0) {
    const modifiedItem = prompt("Modify the last item:");
    if (modifiedItem) {
      itemList.lastChild.textContent = modifiedItem;
    }
  }
});
