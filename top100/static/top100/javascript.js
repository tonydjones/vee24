function reveal(div_id, btn_id) {
  if (document.querySelector(`#${div_id}`).style.display === 'block'){
      document.querySelector(`#${div_id}`).style.display = 'none';
      document.querySelector(`#${btn_id}`).value = "More Details";
  }
  else {
      document.querySelector(`#${div_id}`).style.display = 'block';
      document.querySelector(`#${btn_id}`).value = "Fewer Details";
  }
}

function reveal_search(form_id, submit_id, btn_id) {
  document.querySelector(`#${form_id}`).style.display = 'block';
  document.querySelector(`#${submit_id}`).style.display = 'block';
  document.querySelector(`#${btn_id}`).style.display = 'none';
}