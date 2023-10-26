$('#people-entry').magicSuggest({
    data: [
      {name: 'Jimmy Hoffa'},
      {name: 'Elvis Presley'},
      {name: 'DB Cooper'},
      {name: 'Marylin Monroe'}
    ]
  })
  
$('.post-form').on('click', '.open-overlay', function(e) {
  e.preventDefault()
  $($(this).data('target'))
    .removeClass('closed')
    .addClass('open')
  $('.post-form-backdrop')
    .removeClass('closed')
})
$('.post-form').on('click', '.post-form-overlay .close', function() {
  $(this).parents('.post-form-overlay')
    .addClass('closed')
    .removeClass('open')
  $('.post-form-backdrop')
    .addClass('closed')
})


let isBold = false;
let isItalic = false;
let isUnderline = false;

function toggleFormat(format) {
    if (format === 'bold') {
        isBold = !isBold;
        document.execCommand('bold', false, null);
    } else if (format === 'italic') {
        isItalic = !isItalic;
        document.execCommand('italic', false, null);
    } else if (format === 'underline') {
        isUnderline = !isUnderline;
        document.execCommand('underline', false, null);
    }

    updateButtonState();
}

function updateButtonState() {
const boldButton = document.getElementById('boldButton');
const italicButton = document.getElementById('italicButton');
const underlineButton = document.getElementById('underlineButton');

boldButton.style.backgroundColor = isBold ? '#3498db' : '';
italicButton.style.backgroundColor = isItalic ? '#3498db' : '';
underlineButton.style.backgroundColor = isUnderline ? '#3498db' : '';
}

function openImageModal() {
    const imageModal = document.getElementById('imageModal');
    imageModal.style.display = 'block';
}

function closeImageModal() {
    const imageModal = document.getElementById('imageModal');
    imageModal.style.display = 'none';
}

function insertImage() {
    const imageUrl = document.getElementById('imageUrl').value;
    if (imageUrl) {
        const image = document.createElement('img');
        image.src = imageUrl;
        const editableContent = document.getElementById('editable-content');
        editableContent.appendChild(image);
        closeImageModal();
    }
}