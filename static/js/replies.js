const editReplyButtons = document.getElementsByClassName("btn-reply-edit");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("commentForm");
const submitReplyButton = document.getElementById("replyButton");

const deleteReplyModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReplyButtons = document.getElementsByClassName("btn-reply-delete");
const deleteReplyConfirm = document.getElementById("deleteConfirm");

for (let button of editReplyButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      console.log(replyId)
      let replyContent = document.getElementById(`reply${replyId}`).innerText;
      console.log(replyContent)
      replyText.value = replyContent;
      submitReplyButton.innerText = "Update";
      replyForm.setAttribute("action", `edit_reply/${replyId}`);
    });
  }

  for (let button of deleteReplyButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete reply?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your reply? This action cannot be undone." 
      deleteReviewConfirm.href = `delete_reply/${replyId}`;
      deleteModal.show();
    });
  }
  

