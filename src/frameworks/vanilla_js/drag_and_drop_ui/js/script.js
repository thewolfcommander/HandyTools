const fill = document.querySelector('.fill');
const empties = document.querySelectorAll('.empty');

// fill listeners 

fill.addEventListener('dragstart', dragStart);
fill.addEventListener('dragend', dragEnd);



// Loop through  empties and call drag events
for (const empty of empties) {
    empty.addEventListener('dragover', dragOver);
    empty.addEventListener('dragenter', dragEnter);
    empty.addEventListener('dragleave', dragLeave);
    empty.addEventListener('drop', dragDrop);
}

// Drag functions 

function dragStart() {
    console.log('start');
    this.className += ' hold';
    setTimeout(() => (this.className = 'invisible'), 0);
}

function dragEnd() {
    console.log('end');
    this.className = 'fill';
}


function dragOver(e) {
    e.preventDefault();
    console.log('over');
}

function dragEnter() {
    console.log('enter');
}

function dragLeave() {
    console.log('leave');
}

function dragDrop() {
    console.log('drop');
}