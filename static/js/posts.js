const deletePostModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("btn-post-delete");
const deletePostConfirm = document.getElementById("deleteConfirm");


  for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete Recipe?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your Recipe? This action cannot be undone." 
      deletePostConfirm.href = `delete_post/${postId}`;
      deleteModal.show();
    });
  }
  