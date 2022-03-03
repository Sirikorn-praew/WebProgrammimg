window.onload = () => {
    const form1 = document.querySelector("#addForm");
  
    let items = document.getElementById("items");
    let submit = document.getElementById("submit");
  
    let editItem = null;
  
    form1.addEventListener("submit", addItem);
    
    // items.addEventListener("dlbclick", editItem_text);
    items.addEventListener("click", removeItem);

};
  
function addItem(e) {
    e.preventDefault();
  
    if (submit.value != "+") {
        console.log("Hello");
  
        editItem.target.parentNode.childNodes[0].data
            = document.getElementById("item").value;
  
        submit.value = "+";
        document.getElementById("item").value = "";
  
        // document.getElementById("lblsuccess").innerHTML
        //     = "Text edited successfully";
  
        document.getElementById("lblsuccess")
                        .style.display = "block";
  
        setTimeout(function() {
            document.getElementById("lblsuccess")
                            .style.display = "none";
        }, 3000);
  
        return false;
    }
  
    let newItem = document.getElementById("item").value;
    if (newItem.trim() == "" || newItem.trim() == null)
        return false;
    else
        document.getElementById("item").value = "";
  
    let li = document.createElement("li");
    li.className = "list-group-item";
  
    let deleteButton = document.createElement("button");
  
    deleteButton.className = 
        "btn-danger btn btn-sm float-right delete";
  
    deleteButton.appendChild(document.createTextNode("Delete"));
  
    let editButton = document.createElement("button");
  
    editButton.className = 
            "btn-success btn btn-sm float-right edit";
  
    editButton.appendChild(document.createTextNode("Edit"));
  
    li.appendChild(document.createTextNode(newItem));
    li.appendChild(deleteButton);
    li.appendChild(editButton);
  
    items.appendChild(li);
}
function saveItem(event) {
	let inputValue = event.target.value;
	if (event.target.value.length > 0 && (event.keyCode === 13 || event.type === 'click')) {
		let li = document.createElement('li');
		li.addEventListener('click', toggleDone);
		li.addEventListener('dblclick', editItem);
		li.textContent = event.target.value;
		event.target.parentNode.prepend(li);
		event.target.remove();
	 } else if (event.target.value.length === 0 && (event.keyCode === 13 || event.type === 'click')) {
		let li = document.createElement('li');
		li.addEventListener('click', toggleDone);
		li.addEventListener('dblclick', editItem);
		li.textContent = initialValue;
		event.target.parentNode.prepend(li);
		event.target.remove();
	}
}
function editItem_text(e) {
    // confirm("Are you Sure?")
    // submit.value = "EDIT";
    let initialValue;
	let itemss = e.target.parentNode;
	itemss = document.createElement('input');
	itemInput.type = 'text';
	itemInput.value = itemss;
	itemInput.classList.add('edit');
	initialValue = itemss;
	itemInput.addEventListener('keypress', saveItem);
	itemInput.addEventListener('click', saveItem);
	e.target.parentNode.prepend(itemInput);
	e.target.remove();
	itemInput.select();
    items.textContent=itemInput
    
}


function removeItem(e) {
    e.preventDefault();
    if (e.target.classList.contains("delete")) {
        if (confirm("Are you Sure?")) {
            let li = e.target.parentNode;
            items.removeChild(li);
            // document.getElementById("lblsuccess").innerHTML
            //     = "Text deleted successfully";
  
            document.getElementById("lblsuccess")
                        .style.display = "block";
  
            setTimeout(function() {
                document.getElementById("lblsuccess")
                        .style.display = "none";
            }, 3000);
        }
    }
    
    if (e.target.classList.contains("edit")) {
        // document.getElementById("item").value =
        //     e.target.parentNode.childNodes[0].data;
        
        // items.textContent=inputValue;
        // editItem_text(e)
        // editItem = e
    }
}
  
function toggleButton(ref, btnID) {
    document.getElementById(btnID).disabled = false;
}