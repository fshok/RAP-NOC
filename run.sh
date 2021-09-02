#!/bin/bash
start_path="/home/fateme/Desktop/simulator"
	cd	$start_path
	rm -f input.txt
	touch input.txt
	echo "start_path="$start_path"" >> input.txt
	echo "dimension(2D, 3D):"
	read dimension
	echo "dimension="$dimension"" >> input.txt

	echo "router_type(you can use a user_defined router or use saved routers(user_defined,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)):"
	read router_type
	echo "router_type="$router_type"" >> input.txt

	echo "R(0.9, 0.99, 0.999, ..., 0.999999999):"
	read R
	echo "R="$R"" >> input.txt

	echo "size(for example: 4 4, 8 8, 4 4 4, 8 8 8):"
	read size
	echo "size="$size"" >> input.txt

	echo "topology(mesh, torus):"
	read topology
	echo "topology="$topology"" >> input.txt

	echo "traffic_type(uniform, hotspot):"
	read traffic_type
	echo "traffic_type="$traffic_type"" >> input.txt

	echo "traffic(saved, new):"
	read traffic
	echo "traffic="$traffic"" >> input.txt

	echo "number_of_faults(for example: 0, 1, 2):"
	read number_of_faults
	echo "number_of_faults="$number_of_faults"" >> input.txt

	echo "threshold:"
	read threshold
	echo "threshold="$threshold"" >> input.txt
	
	cp	input.txt	../simulator/Topology
	cd	../simulator/Topology
	python3	topology.py
	cd ..
	cp	../simulator/Topology/network.txt	../simulator/Traffic_generator/network.txt
	cp	../simulator/Topology/network.txt	../simulator/Routing/network.txt
	cp	../simulator/Topology/output_topology.txt	../simulator/Routing/output_topology.txt
	if [ $traffic == 'new' ]
	then
		rm -f ../simulator/Routing/traffic_hotspot.txt
		rm -f ../simulator/Routing/traffic_uniform.txt
		touch ../simulator/Routing/traffic_uniform.txt
		touch ../simulator/Routing/traffic_hotspot.txt
		cd	../simulator/Traffic_generator
		python3	uniform_generator.py
		python3 hotspot_generator.py
		cd ..
		cp	../simulator/Traffic_generator/traffic_uniform.txt	../simulator/Routing
		cp	../simulator/Traffic_generator/traffic_hotspot.txt	../simulator/Routing
	else
		rm -f ../simulator/Routing/traffic_hotspot.txt
		rm -f ../simulator/Routing/traffic_uniform.txt
		touch ../simulator/Routing/traffic_uniform.txt
		touch ../simulator/Routing/traffic_hotspot.txt
		if [ $dimension == '2D' ]
		then
			if [ "$size" == '4 4' ]
			then
				cp	../simulator/Traffic_generator/saved_traffics/2D_4*4_traffic_uniform.txt	../simulator/Routing/traffic_uniform.txt
				cp	../simulator/Traffic_generator/saved_traffics/2D_4*4_traffic_hotspot.txt	../simulator/Routing/traffic_hotspot.txt
			fi
			if [ "$size" == '8 8' ]
			then
				cp	../simulator/Traffic_generator/saved_traffics/2D_8*8_traffic_uniform.txt	../simulator/Routing/traffic_uniform.txt
				cp	../simulator/Traffic_generator/saved_traffics/2D_8*8_traffic_hotspot.txt	../simulator/Routing/traffic_hotspot.txt
			fi
		else
			if [ "$size" == '4 4 4' ]
			then
				cp	../simulator/Traffic_generator/saved_traffics/3D_4*4*4_traffic_uniform.txt	../simulator/Routing/traffic_uniform.txt
				cp	../simulator/Traffic_generator/saved_traffics/3D_4*4*4_traffic_hotspot.txt	../simulator/Routing/traffic_hotspot.txt
			fi
			if [ "$size" == '8 8 8' ]
			then
				cp	../simulator/Traffic_generator/saved_traffics/3D_8*8*8_traffic_uniform.txt	../simulator/Routing/traffic_uniform.txt
				cp	../simulator/Traffic_generator/saved_traffics/3D_8*8*8_traffic_hotspot.txt	../simulator/Routing/traffic_hotspot.txt
			fi
		fi
	fi
	cd	../simulator/Routing
	if [ $dimension == '2D' ]
	then
		python3	routing_2D.py
	fi
	if [ $dimension == '3D' ]
	then
		python3	routing_3D.py
	fi
