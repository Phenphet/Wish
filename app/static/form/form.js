const Submit = () => {
    const Form_data = {
        'fullname': $('#fullname').val(),
        'wish': $('#wish').val()
    }
    $.ajax({
        url : '/form/wish/',
        method : 'POST',
        data : Form_data,
        success : function(response) {
            Clear_form()
            if (response.error && Array.isArray(response.data) && response.data.length > 0) {
                    alert(`${response.error} คำหยาบ ${response.data}`)
            }else if(response.error){
                alert(`${response.error}`)
            }else{
                alert(`${response.success}`)
            }
        },
        error: function(xhr, status, error){
            console.error('Error:', error)
        }
    })
}
const Clear_form = () => {
    $('#fullname').val('') 
    $('#wish').val('')
}