document.addEventListener("DOMContentLoaded", function() {
    const formattedContent = document.getElementById('formatted-content');
    formattedContent.innerHTML = formattedContent.innerHTML
        .replace(/\[bold\](.*?)\[\/bold\]/g, '<strong>$1</strong>')
        .replace(/\[italic\](.*?)\[\/italic\]/g, '<em>$1</em>')
        .replace(/\[underline\](.*?)\[\/underline\]/g, '<u>$1</u>');
});