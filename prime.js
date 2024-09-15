function parseDateString(dateString) {
    // Define regular expression patterns to match the expected formats
    const patterns = [
      /^(\d{2})\/(\d{2})\/(\d{4})$/, // DD/MM/YYYY
      /^(\d{4})-(\d{2})-(\d{2})$/,    // YYYY-MM-DD
      /^(\d{1,2}) (\w{3}) (\d{4})$/,  // D MMM YYYY
      /^(\d{1,2}) (\w{3}) (\d{2})$/   // D MMM YY
    ];
  
    // Iterate over each pattern and try to match the input string
    for (const pattern of patterns) {
      const match = pattern.exec(dateString);
      if (match) {
        let day, month, year;
        if (pattern === patterns[0]) {
          // DD/MM/YYYY format
          day = parseInt(match[1], 10);
          month = parseInt(match[2], 10) - 1; // Months are zero-based
          year = parseInt(match[3], 10);
        } else if (pattern === patterns[1]) {
          // YYYY-MM-DD format
          year = parseInt(match[1], 10);
          month = parseInt(match[2], 10) - 1; // Months are zero-based
          day = parseInt(match[3], 10);
        } else {
          // D MMM YYYY or D MMM YY format
          day = parseInt(match[1], 10);
          month = parseMonth(match[2]);
          year = parseInt(match[3], 10);
          if (year < 100) {
            // If year is in YY format, convert it to YYYY format
            year += 2000;
          }
        }
  
        // Create a new Date object with the parsed components
        const date = new Date(year, month, day);
  
        // Check if the parsed date is valid
        if (isNaN(date.getTime())) {
          // If the parsed date is invalid (e.g., February 30th), return null
          return null;
        }
  
        // Return the parsed date as a string in the desired format (e.g., "Sat May 19 2024")
        return date.toString();
      }
    }
  
    // If none of the patterns match, return null
    return null;
  }
  
  // Helper function to parse month abbreviation to month index
  function parseMonth(monthStr) {
    const months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'];
    const index = months.findIndex(m => m.toLowerCase() === monthStr.toLowerCase());
    return index >= 0 ? index : NaN;
  }
  
  // Test the function with different date formats
  console.log(parseDateString('19/05/2024')); // DD/MM/YYYY
  console.log(parseDateString('2023-09-01')); // YYYY-MM-DD
  console.log(parseDateString('4 feb 2024')); // D MMM YYYY
  console.log(parseDateString('19/9/23'));    // DD/MM/YY
  