
const form = document.getElementById('articleForm');
const previewTitle = document.getElementById('preview-title');
const previewContent = document.getElementById('preview-content');
const articlePreview = document.getElementById('articlePreview');


form.addEventListener('submit', (event) => {
    event.preventDefault(); 

    
    const title = form.title.value;
    const content = form.content.value;

   
    previewTitle.textContent = title;
    previewContent.textContent = content;

    
    articlePreview.style.display = 'block';
});
