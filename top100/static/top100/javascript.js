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

function reveal_search(div_id, btn_id) {
  document.querySelector(`#${div_id}`).style.display = 'block';
  document.querySelector(`#${btn_id}`).style.display = 'none';
}