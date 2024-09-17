document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('ambulance-booking-form');
    const bookingsList = document.getElementById('bookings');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const size = document.getElementById('size').value;
        const pickUpPoint = document.getElementById('pick-up-point').value;
        const hospital = document.getElementById('hospital').value;
        const dateTime = document.getElementById('date-time').value;

        // Create a new list item for the booking
        const listItem = document.createElement('li');
        listItem.textContent = `Ambulance Size: ${size}, Pick-Up Point: ${pickUpPoint}, Hospital: ${hospital}, Date & Time: ${dateTime}`;
        
        // Append the new booking to the list
        bookingsList.appendChild(listItem);

        // Clear the form
        form.reset();
    });
});
