import React, { useEffect, useState } from "react";
import axios from "axios";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';

// Fix for default marker icon issue in Leaflet
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require('leaflet/dist/images/marker-icon-2x.png'),
  iconUrl: require('leaflet/dist/images/marker-icon.png'),
  shadowUrl: require('leaflet/dist/images/marker-shadow.png'),
});

function App() {
  const [vehicles, setVehicles] = useState([]);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/vehicles")
      .then(response => {
        setVehicles(response.data);
    })
      .catch(error => console.error("Error fetching vehicles:", error));
  }, []);

  return (
    <div>
      <h1>My Fleet Map</h1>
      <MapContainer center={[20.5937, 78.9629]} zoom={5} style={{ height: "600px", width: "100%" }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        {vehicles && vehicles.map(vehicle => (
          <Marker key={vehicle.id} position={[vehicle.lat, vehicle.lng]}>
            <Popup>
              {vehicle.name}
              <br />
              Lat: {vehicle.lat}, Lng: {vehicle.lng}
            </Popup>
          </Marker>
        ))}
      </MapContainer>
    </div>
  );
}

export default App;
