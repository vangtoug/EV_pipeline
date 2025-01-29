SELECT 
    state,
    COUNT(*) AS total_count


FROM 
    `electric-vehicle-448005.electric_vehicle_dataset.ev_dim`


GROUP BY 
    state
ORDER BY 
    total_count desc
    