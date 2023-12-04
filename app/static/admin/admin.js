$(document).ready( () => {
    $('#myTable').DataTable()
})
const Delete = (IdData) =>{
    // alert(data_id)
    const id  ={
        'id': IdData
    }
    $.ajax({
        url : '/wish/admin/table',
        method : 'POST',
        data : id,
        success : (response) => {
            console.log(response)
            if(response.success){
                window.location.href = '/wish/admin/table'
            }
        },
        error : (xhr, status, error) => {
            console.error('Error:', error)
        }
    })
}