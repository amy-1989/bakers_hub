const editReplyButtons = document.getElementsByClassName("btn-reply-edit");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("commentForm");
const submitReplyButton = document.getElementById("replyButton");


for (let button of editReplyButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      let replyContent = document.getElementById(`reply${replyId}`).innerText;
      replyText.value = replyContent;
      submitReplyButton.innerText = "Update";
      replyForm.setAttribute("action", `edit_reply/${replyId}`);
    });
  }



