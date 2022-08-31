const btnAddNew = document.querySelector("#add-new");
const formSection = document.querySelector(".form-section");
const mainForm = document.querySelector("#mainForm");
const btnCancel = document.querySelector(".btn--cancel");
const btnAccept = document.querySelector(".btn--accept");
const tableDeleteBtn = document.querySelector(".table__edit-btn");
const tableEditBtn = document.querySelector(".table__delete-btn");
// Table
const tableContainer = document.querySelector(".table-container");
const table = document.createElement("table");
const thead = document.createElement("thead");
const thr = document.createElement("tr");
const tbody = document.createElement("tbody");
const heading = ["#", "Username", "Password", "Fullname", "Action"]

table.className = "table";
thead.className = "table__thead";
thr.className = "table__head-row";

heading.map( h => thr.insertAdjacentHTML("beforeend",  `<th class="table__heading">${h}</th>`));



// AddEventListener
btnAddNew.addEventListener("click", addNew);
if( btnCancel ) btnCancel.addEventListener("click", cancelAddNew);
if( btnAccept ) mainForm.addEventListener("submit", addUserData)
tableContainer.addEventListener("click", tableActions);

getUsers();

function addNew(e){
    e.preventDefault();
    formSection.style.display = "grid";
    mainForm.fullname.focus();
}

function cancelAddNew(){
    formSection.style.display = "none";
}
//? Agrega a un usuario 
async function addUserData(e){
    e.preventDefault();


    const formData = new FormData(mainForm);
    
     const data = await fetch("/add", {
        'method':"POST",
        'Content-Type': 'application/json;charset=utf-8',
        'body':formData
    });

    const {insertedRow} = await data.json();
    if( insertedRow > 0  ) getUsers();
    this.reset();
    mainForm.fullname.focus();
}



//? Captura todos los usuarios y los muestra por pantalla
async function getUsers(){
    const {data} = await (await fetch("/getUsers", {
        'method':"POST",
        'Content-Type': 'application/json;charset=utf-8'
    })).json();

    
    if( data.length > 0 ){
        renderTable(data);
        table.appendChild(tbody);
        tableContainer.append(table);
    }

    if( data.length <= 0  ) tableContainer.innerHTML = "";
}

async function tableActions(e){
    e.preventDefault();
    if(e.target.classList.contains("table__delete-btn") || e.target.classList.contains("table__icon-delete")){
        const rowId = e.target.parentElement.parentElement.dataset.action || e.target.parentElement.parentElement.parentElement.dataset.action;
        
        const deleteData = new FormData();
        deleteData.append('id', rowId);

        const data = await fetch("/delete", {
            'method':"POST",
            'Content-Type': 'application/json;charset=utf-8',
            'body':deleteData
        })
        
        const {deleted:{id}} = await data.json();

        if(id > 0) getUsers();
    }
   
}

function renderTable(data = []){
    thead.appendChild(thr);
    tbody.className = "table__tbody";
    tbody.innerHTML = '';
    table.appendChild(thead);
     data.forEach(({fullname, id, password, username}, index)=>{
        tbody.innerHTML += `<tr class="table__tbody-row">
            <td class="table__data">${index + 1}</td>
            <td class="table__data">${username}</td>
            <td class="table__data">${password}</td>
            <td class="table__data">${fullname}</td>
            <td class="table__data" data-action="${id}">
                <div class="table__buttons">
                    <button type="button" class="table__edit-btn table__btn">
                    <img class="table__icon table__icon-edit" src="/icons/edit.svg" alt="edit">
                    </button>
                    <span class="table__separator">||</span>
                    <button type="button" class="table__delete-btn table__btn">
                        <img class="table__icon table__icon-delete" src="/icons/delete.svg" alt="delete">
                    </button>
                </div>
            </td>
        </tr>`;
        });
}

