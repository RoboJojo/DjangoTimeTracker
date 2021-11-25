function formatDurationChar(el) {
    el.value = el.value.replace(/[^\d:-]/g,'');
}

function edited(el) {
    el.dataset.changed = "true";
}

$('#edit-project-form').submit((event) => {
    event.preventDefault();
    data = [];
    $('#edit-project-table-body').find('tr[data-changed="true"]').each(function () {
        let tds = this.getElementsByTagName('td');
        data.push(
            {
                id : this.getElementsByTagName('th')[0].innerHTML,
                name : tds[0].children[0].value,
                timeSpent : tds[1].children[0].value,
                start_date : tds[2].children[0].value
            }
        );
    });
    $.ajax({
        url: '/editProject/',
        type: 'POST',
        data: {
            data : JSON.stringify(data), 
            csrfmiddlewaretoken : $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(result) {
            if (result.success) {
                $('#success-toast').removeClass('bg-danger');
                $('#success-toast').addClass('bg-theme');                
                $('#success-toast-body').html("Success! Changes are made");
                $('#success-toast').toast('show'); 
            }          
            else {
                $('#success-toast').removeClass('bg-theme');
                $('#success-toast').addClass('bg-danger');
                $('#success-toast-body').html("Failure to make changes");
                $('#success-toast').toast('show'); 
            }  
        }               
    });
});