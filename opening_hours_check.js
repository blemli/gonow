const opening_hours = require("opening_hours");
const process = require("process");

function main() {
    // Check if opening hours string and timestamp are provided
    if (process.argv.length < 4) {
        console.error("Usage: node opening_hours_check.js '<opening_hours>' '<timestamp>'");
        process.exit(1);
    }

    const openingHoursString = process.argv[2];
    const timestamp = parseInt(process.argv[3], 10);
    const date = new Date(timestamp);

    // Initialize opening_hours object
    var oh = new opening_hours(openingHoursString);

    // Get open state and next change
    const isOpen = oh.getState(date);
    let nextChange = oh.getNextChange(date);

    // Adjust nextChange to be more friendly for JSON output
    if (nextChange) {
        nextChange = nextChange.getTime();
    }

    // Output results
    const result = {
        is_open: isOpen,
        next_change: nextChange
    };
    console.log(JSON.stringify(result));
}

main();
