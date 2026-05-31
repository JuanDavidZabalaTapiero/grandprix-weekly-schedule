export async function screenshot(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (err) {
    throw err;
  }
}

export async function changeWeekTimeSlotInstructor(url, data) {
  try {
    const response = await fetch(url, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const dataReceived = await response.json();
    return dataReceived;
  } catch (err) {
    throw err;
  }
}

export async function changeClass(url, data) {
  try {
    const response = await fetch(url, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    const dataReceived = await response.json();
    return dataReceived;
  } catch (err) {
    throw err;
  }
}
