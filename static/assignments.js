function submitVideo(assignmentId){
    const input = document.querySelector(`.video-upload[data-assignment="${assignmentId}"]`);
    const file = input.files[0];

    if(!file){
        alert("Please select a video first!");
        return;
    }

    // Mock sending to backend
    setTimeout(() => {
        const statusSpan = input.parentElement.querySelector('.status');
        statusSpan.textContent = "Submitted";
        statusSpan.style.color = "#00ff00"; // green for success
        alert(`Assignment ${assignmentId} submitted successfully!`);
    }, 500);

    // Real backend integration:
    // Use fetch() with FormData to send the video to Django backend API
    /*
    const formData = new FormData();
    formData.append('video', file);
    formData.append('assignment_id', assignmentId);

    fetch('http://127.0.0.1:8000/api/assignments/upload/', {
        method: 'POST',
        body: formData,
        headers: {
            'Authorization': 'Bearer ' + accessToken
        }
    }).then(response => response.json())
      .then(data => {
          // update status
      });
    */
}