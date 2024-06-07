
function deletea(){
    Swal.fire({
  title: "Are you sure?",
  text: "You won't be able to revert this!",
  icon: "warning",
  showCancelButton: true,
  confirmButtonColor: "#3085d6",
  cancelButtonColor: "#d33",
  confirmButtonText: "Yes, delete it!"
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire({
      title: "Deleted!",
      text: "Your file has been deleted.",
      icon: "success"
    });
  }
});}

        function saved(){
          
         
          Swal.fire({
  position: "center",
  icon: "success",
  title: "Your work has been saved",
  showConfirmButton: false,
  timer:5,
});
        }
        function upadte(){
          Swal.fire({
  position: "center",
  icon: "success",
  title: "Your work has been Updated!",
  showConfirmButton: true,
  timer:5000,
});
        }

