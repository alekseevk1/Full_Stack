function dropDownMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
  }
    // Закрыть раскрывающийся список, если пользователь щелкнет за его пределами.
    window.onclick = function(event) {
      if (!event.target.matches('.button_catalog')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
      }
    }

console.log("Hell")

/*const productsBox = document.getElementById('products-box')
const spinnerBox = document.getElementById('spinner-box')
const loadBtn = document.getElementById('load-btn')
const loadBox = document.getElementById('loading-box')
let visible = 3

const handleGetData = () => {
  $.ajax({
    type: 'GET',
    //url: ``
    success: function(response){
      const data = response.data
      data.map(post=>{console.log(product.id)
      })
    },
    error: function(error){
      console.log(error)
    }
  })
}

handleGetData()

loadBtn.addEventListener('click', ()=>{
  visible += 3
  handleGetData()
})*/

const loadBtn = document.getElementById('btn');
const spinner = document.getElementById('spinner');
const total = JSON.parse(document.getElementById('json-total').textContent);
console.log(total)
const alert = document.getElementById('alert');

function loadmorePost() {
    var _current_item = $('.single_content').length
    const content_container = document.getElementById("content");
    $.ajax({
        url: '{% url "load" %}',
        type: 'GET',
        data: {
            'offset': _current_item
        },
        beforeSend: function () {
            loadBtn.classList.add('not-visible');
            spinner.classList.remove('not-visible');
        },
        success: function (response) {
            const data = response.products
            spinner.classList.add('not-visible')
            data.map(product => {
                console.log(product.title);
                content_container.innerHTML += `<div class="single_content border border-success mt-2 pl-2">
                                                    <h3>${product.title}</h3>
                                                    <p>${product.desc}</p>
                                                </div>`
            })
            if (_current_item == total) {
                alert.classList.remove('not-visible');
            } else {
                loadBtn.classList.remove('not-visible');
            }
        },
        error: function (err) {
            console.log(err);
        },
    });
}

loadBtn.addEventListener('click', () => {
    loadmorePost()
});