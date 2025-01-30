SELECT

    `electric vehicle type`,
    COUNT(*) AS total_count


FROM 
    `electric-vehicle-448005.electric_vehicle_dataset.ev_dim`


GROUP BY 
    `electric vehicle type`
ORDER BY 
    total_count desc