const editPostButtons = document.getElementsByClassName("btn-post-edit");
const postText = document.getElementById("id_body");
const postForm = document.getElementById("postForm");
const submitPostButton = document.getElementById("submitPostButton");

const deletePostModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("btn-post-delete");
const deletePostConfirm = document.getElementById("deleteConfirm");

for (let button of editPostButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      console.log(postId)
      let postContent = document.getElementById(`post${postId}`).innerText;
      postText.value = postContent;
      console.log(postContent)
      submitPostButton.innerText = "Update";
      postForm.setAttribute("action", `edit_post/${postId}`);
    });
  }


  for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
      let postId = e.target.getAttribute("post_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete Recipe?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your Recipe? This action cannot be undone." 
      deletePostConfirm.href = `delete_post/${postId}`;
      deleteModal.show();
    });
  }
  