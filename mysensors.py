#
# pythonized version oy MyMessage.h from MySensors library, 
# see https://github.com/mysensors/MySensors/blob/development/core/MyMessage.h
#

from enum import Enum, IntEnum

class Commands(IntEnum):
    C_PRESENTATION = 0  	#!< Sent by a node when they present attached sensors. This is usually done in presentation() at startup.
    C_SET = 1	            #!< This message is sent from or to a sensor when a sensor value should be updated.
    C_REQ = 2	            #!< Requests a variable value (usually from an actuator destined for controller).
    C_INTERNAL = 3	        #!< Internal MySensors messages (also include common messages provided/generated by the library).
    C_STREAM = 4	        #!< For firmware and other larger chunks of data that need to be divided into pieces.    

command_names = {
    0: "C_PRESENTATION",	# Sent by a node when they present attached sensors. This is usually done in presentation() at startup.
    1: "C_SET",	            # This message is sent from or to a sensor when a sensor value should be updated.
    2: "C_REQ",	            # Requests a variable value (usually from an actuator destined for controller).
    3: "C_INTERNAL",	    # Internal MySensors messages (also include common messages provided/generated by the library).
    4: "C_STREAM",	        # For firmware and other larger chunks of data that need to be divided into pieces.
}

class Sensors(IntEnum):
    S_DOOR = 0	            #!< Door sensor, V_TRIPPED, V_ARMED
    S_MOTION = 1	        #!< Motion sensor, V_TRIPPED, V_ARMED
    S_SMOKE = 2	            #!< Smoke sensor, V_TRIPPED, V_ARMED
    S_BINARY = 3	        #!< Binary light or relay, V_STATUS, V_WATT
    S_DIMMER = 4	        #!< Dimmable light or fan device, V_STATUS (on/off), V_PERCENTAGE (dimmer level 0-100), V_WATT
    S_COVER = 5	            #!< Blinds or window cover, V_UP, V_DOWN, V_STOP, V_PERCENTAGE (open/close to a percentage)
    S_TEMP = 6	            #!< Temperature sensor, V_TEMP
    S_HUM = 7	            #!< Humidity sensor, V_HUM
    S_BARO = 8	            #!< Barometer sensor, V_PRESSURE, V_FORECAST
    S_WIND = 9	            #!< Wind sensor, V_WIND, V_GUST
    S_RAIN = 10	            #!< Rain sensor, V_RAIN, V_RAINRATE
    S_UV = 11	            #!< Uv sensor, V_UV
    S_WEIGHT = 12	        #!< Personal scale sensor, V_WEIGHT, V_IMPEDANCE
    S_POWER = 13	        #!< Power meter, V_WATT, V_KWH, V_VAR, V_VA, V_POWER_FACTOR
    S_HEATER = 14	        #!< Header device, V_HVAC_SETPOINT_HEAT, V_HVAC_FLOW_STATE, V_TEMP
    S_DISTANCE = 15	        #!< Distance sensor, V_DISTANCE
    S_LIGHT_LEVEL = 16	    #!< Light level sensor, V_LIGHT_LEVEL (uncalibrated in percentage),  V_LEVEL (light level in lux)
    S_ARDUINO_NODE = 17	    #!< Used (internally) for presenting a non-repeating Arduino node
    S_ARDUINO_REPEATER_NODE = 18	#!< Used (internally) for presenting a repeating Arduino node
    S_LOCK = 19	            #!< Lock device, V_LOCK_STATUS
    S_IR = 20	            #!< IR device, V_IR_SEND, V_IR_RECEIVE
    S_WATER = 21	        #!< Water meter, V_FLOW, V_VOLUME
    S_AIR_QUALITY = 22  	#!< Air quality sensor, V_LEVEL
    S_CUSTOM = 23	        #!< Custom sensor
    S_DUST = 24	            #!< Dust sensor, V_LEVEL
    S_SCENE_CONTROLLER = 25	#!< Scene controller device, V_SCENE_ON, V_SCENE_OFF.
    S_RGB_LIGHT = 26	    #!< RGB light. Send color component data using V_RGB. Also supports V_WATT
    S_RGBW_LIGHT = 27	    #!< RGB light with an additional White component. Send data using V_RGBW. Also supports V_WATT
    S_COLOR_SENSOR = 28	    #!< Color sensor, send color information using V_RGB
    S_HVAC = 29	            #!< Thermostat/HVAC device. V_HVAC_SETPOINT_HEAT, V_HVAC_SETPOINT_COLD, V_HVAC_FLOW_STATE, V_HVAC_FLOW_MODE, V_TEMP
    S_MULTIMETER = 30	    #!< Multimeter device, V_VOLTAGE, V_CURRENT, V_IMPEDANCE
    S_SPRINKLER = 31	    #!< Sprinkler, V_STATUS (turn on/off), V_TRIPPED (if fire detecting device)
    S_WATER_LEAK = 32	    #!< Water leak sensor, V_TRIPPED, V_ARMED
    S_SOUND = 33	        #!< Sound sensor, V_TRIPPED, V_ARMED, V_LEVEL (sound level in dB)
    S_VIBRATION = 34	    #!< Vibration sensor, V_TRIPPED, V_ARMED, V_LEVEL (vibration in Hz)
    S_MOISTURE = 35	        #!< Moisture sensor, V_TRIPPED, V_ARMED, V_LEVEL (water content or moisture in percentage?)
    S_INFO = 36	            #!< LCD text device / Simple information device on controller, V_TEXT
    S_GAS = 37	            #!< Gas meter, V_FLOW, V_VOLUME
    S_GPS = 38	            #!< GPS Sensor, V_POSITION
    S_WATER_QUALITY = 39	#!< V_TEMP, V_PH, V_ORP, V_EC, V_STATUS

sensor_names = {
    -1: "(node)",
    0: "S_DOOR",	        # Door sensor, V_TRIPPED, V_ARMED
    1: "S_MOTION",	        # Motion sensor, V_TRIPPED, V_ARMED
    2: "S_SMOKE",	        # Smoke sensor, V_TRIPPED, V_ARMED
    3: "S_BINARY",	        # Binary light or relay, V_STATUS, V_WATT
    # 3: "S_LIGHT",	        # \deprecated Same as S_BINARY
    4: "S_DIMMER",	        # Dimmable light or fan device, V_STATUS (on/off), V_PERCENTAGE (dimmer level 0-100), V_WATT
    5: "S_COVER",	        # Blinds or window cover, V_UP, V_DOWN, V_STOP, V_PERCENTAGE (open/close to a percentage)
    6: "S_TEMP",	        # Temperature sensor, V_TEMP
    7: "S_HUM",	            # Humidity sensor, V_HUM
    8: "S_BARO",	        # Barometer sensor, V_PRESSURE, V_FORECAST
    9: "S_WIND",	        # Wind sensor, V_WIND, V_GUST
    10: "S_RAIN",	        # Rain sensor, V_RAIN, V_RAINRATE
    11: "S_UV",	            # Uv sensor, V_UV
    12: "S_WEIGHT",	        # Personal scale sensor, V_WEIGHT, V_IMPEDANCE
    13: "S_POWER",	        # Power meter, V_WATT, V_KWH, V_VAR, V_VA, V_POWER_FACTOR
    14: "S_HEATER",	        # Header device, V_HVAC_SETPOINT_HEAT, V_HVAC_FLOW_STATE, V_TEMP
    15: "S_DISTANCE",	    # Distance sensor, V_DISTANCE
    16: "S_LIGHT_LEVEL",	# Light level sensor, V_LIGHT_LEVEL (uncalibrated in percentage),  V_LEVEL (light level in lux)
    17: "S_ARDUINO_NODE",	# Used (internally) for presenting a non-repeating Arduino node
    18: "S_ARDUINO_REPEATER_NODE",	# Used (internally) for presenting a repeating Arduino node
    19: "S_LOCK",	        # Lock device, V_LOCK_STATUS
    20: "S_IR",	            # IR device, V_IR_SEND, V_IR_RECEIVE
    21: "S_WATER",	        # Water meter, V_FLOW, V_VOLUME
    22: "S_AIR_QUALITY",	# Air quality sensor, V_LEVEL
    23: "S_CUSTOM",	        # Custom sensor
    24: "S_DUST",	        # Dust sensor, V_LEVEL
    25: "S_SCENE_CONTROLLER",	# Scene controller device, V_SCENE_ON, V_SCENE_OFF.
    26: "S_RGB_LIGHT",	    # RGB light. Send color component data using V_RGB. Also supports V_WATT
    27: "S_RGBW_LIGHT",	    # RGB light with an additional White component. Send data using V_RGBW. Also supports V_WATT
    28: "S_COLOR_SENSOR",	# Color sensor, send color information using V_RGB
    29: "S_HVAC",	        # Thermostat/HVAC device. V_HVAC_SETPOINT_HEAT, V_HVAC_SETPOINT_COLD, V_HVAC_FLOW_STATE, V_HVAC_FLOW_MODE, V_TEMP
    30: "S_MULTIMETER",	    # Multimeter device, V_VOLTAGE, V_CURRENT, V_IMPEDANCE
    31: "S_SPRINKLER",	    # Sprinkler, V_STATUS (turn on/off), V_TRIPPED (if fire detecting device)
    32: "S_WATER_LEAK",	    # Water leak sensor, V_TRIPPED, V_ARMED
    33: "S_SOUND",	        # Sound sensor, V_TRIPPED, V_ARMED, V_LEVEL (sound level in dB)
    34: "S_VIBRATION",	    # Vibration sensor, V_TRIPPED, V_ARMED, V_LEVEL (vibration in Hz)
    35: "S_MOISTURE",	    # Moisture sensor, V_TRIPPED, V_ARMED, V_LEVEL (water content or moisture in percentage?)
    36: "S_INFO",	        # LCD text device / Simple information device on controller, V_TEXT
    37: "S_GAS",	        # Gas meter, V_FLOW, V_VOLUME
    38: "S_GPS",	        # GPS Sensor, V_POSITION
    39: "S_WATER_QUALITY",	# V_TEMP, V_PH, V_ORP, V_EC, V_STATUS
}

class Values(IntEnum):
    V_TEMP = 0	            #!< S_TEMP. Temperature S_TEMP, S_HEATER, S_HVAC
    V_HUM = 1	            #!< S_HUM. Humidity
    V_STATUS = 2	        #!< S_BINARY, S_DIMMER, S_SPRINKLER, S_HVAC, S_HEATER. Used for setting/reporting binary (on/off) status. 1=on, 0=off
    V_PERCENTAGE = 3	    #!< S_DIMMER. Used for sending a percentage value 0-100 (%).
    V_PRESSURE = 4	        #!< S_BARO. Atmospheric Pressure
    V_FORECAST = 5	        #!< S_BARO. Whether forecast. string of "stable", "sunny", "cloudy", "unstable", "thunderstorm" or "unknown"
    V_RAIN = 6	            #!< S_RAIN. Amount of rain
    V_RAINRATE = 7	        #!< S_RAIN. Rate of rain
    V_WIND = 8	            #!< S_WIND. Wind speed
    V_GUST = 9	            #!< S_WIND. Gust
    V_DIRECTION = 10	    #!< S_WIND. Wind direction 0-360 (degrees)
    V_UV = 11	            #!< S_UV. UV light level
    V_WEIGHT = 12	        #!< S_WEIGHT. Weight(for scales etc)
    V_DISTANCE = 13	        #!< S_DISTANCE. Distance
    V_IMPEDANCE = 14	    #!< S_MULTIMETER, S_WEIGHT. Impedance value
    V_ARMED = 15	        #!< S_DOOR, S_MOTION, S_SMOKE, S_SPRINKLER. Armed status of a security sensor. 1 = Armed, 0 = Bypassed
    V_TRIPPED = 16	        #!< S_DOOR, S_MOTION, S_SMOKE, S_SPRINKLER, S_WATER_LEAK, S_SOUND, S_VIBRATION, S_MOISTURE.
    V_WATT = 17	            #!< S_POWER, S_BINARY, S_DIMMER, S_RGB_LIGHT, S_RGBW_LIGHT. Watt value for power meters
    V_KWH = 18	            #!< S_POWER. Accumulated number of KWH for a power meter
    V_SCENE_ON = 19	        #!< S_SCENE_CONTROLLER. Turn on a scene
    V_SCENE_OFF = 20	    #!< S_SCENE_CONTROLLER. Turn of a scene
    V_HEATER = 21	        #!< \deprecated Same as V_HVAC_FLOW_STATE
    V_HVAC_SPEED = 22	    #!< S_HVAC, S_HEATER. HVAC/Heater fan speed ("Min", "Normal", "Max", "Auto")
    V_LIGHT_LEVEL = 23	    #!< S_LIGHT_LEVEL. Uncalibrated light level. 0-100%. Use V_LEVEL for light level in lux
    V_VAR1 = 24	            #!< VAR1
    V_VAR2 = 25	            #!< VAR2
    V_VAR3 = 26	            #!< VAR3
    V_VAR4 = 27	            #!< VAR4
    V_VAR5 = 28	            #!< VAR5
    V_UP = 29	            #!< S_COVER. Window covering. Up
    V_DOWN = 30	            #!< S_COVER. Window covering. Down
    V_STOP = 31	            #!< S_COVER. Window covering. Stop
    V_IR_SEND = 32	        #!< S_IR. Send out an IR-command
    V_IR_RECEIVE = 33	    #!< S_IR. This message contains a received IR-command
    V_FLOW = 34	            #!< S_WATER. Flow of water (in meter)
    V_VOLUME = 35	        #!< S_WATER. Water volume
    V_LOCK_STATUS = 36	    #!< S_LOCK. Set or get lock status. 1=Locked, 0=Unlocked
    V_LEVEL = 37	        #!< S_DUST, S_AIR_QUALITY, S_SOUND (dB), S_VIBRATION (hz), S_LIGHT_LEVEL (lux)
    V_VOLTAGE = 38	        #!< S_MULTIMETER
    V_CURRENT = 39	        #!< S_MULTIMETER
    V_RGB = 40	            #!< S_RGB_LIGHT, S_COLOR_SENSOR. Sent as ASCII hex: RRGGBB (RR=red, GG=green, BB=blue component)
    V_RGBW = 41	            #!< S_RGBW_LIGHT. Sent as ASCII hex: RRGGBBWW (WW=white component)
    V_ID = 42	            #!< Used for sending in sensors hardware ids (i.e. OneWire DS1820b).
    V_UNIT_PREFIX = 43	    #!< Allows sensors to send in a string representing the unit prefix to be displayed in GUI, not parsed by controller! E.g. cm, m, km, inch.
    V_HVAC_SETPOINT_COOL = 44	#!< S_HVAC. HVAC cool setpoint (Integer between 0-100)
    V_HVAC_SETPOINT_HEAT = 45	#!< S_HEATER, S_HVAC. HVAC/Heater setpoint (Integer between 0-100)
    V_HVAC_FLOW_MODE = 46	#!< S_HVAC. Flow mode for HVAC ("Auto", "ContinuousOn", "PeriodicOn")
    V_TEXT = 47	            #!< S_INFO. Text message to display on LCD or controller device
    V_CUSTOM = 48	        #!< Custom messages used for controller/inter node specific commands, preferably using S_CUSTOM device type.
    V_POSITION = 49	        #!< GPS position and altitude. Payload: latitude;longitude;altitude(m). E.g. "55.722526;13.017972;18"
    V_IR_RECORD = 50	    #!< Record IR codes S_IR for playback
    V_PH = 51	            #!< S_WATER_QUALITY, water PH
    V_ORP = 52	            #!< S_WATER_QUALITY, water ORP : redox potential in mV
    V_EC = 53	            #!< S_WATER_QUALITY, water electric conductivity μS/cm (microSiemens/cm)
    V_VAR = 54	            #!< S_POWER, Reactive power: volt-ampere reactive (var)
    V_VA = 55	            #!< S_POWER, Apparent power: volt-ampere (VA)
    V_POWER_FACTOR = 56	    #!< S_POWER, Ratio of real power to apparent power: floating point value in the range [-1,..,1]

value_names = {
    -1: "I_BATTERY_LEVEL",
    0: "V_TEMP",	        # S_TEMP. Temperature S_TEMP, S_HEATER, S_HVAC
    1: "V_HUM",	            # S_HUM. Humidity
    2: "V_STATUS",	        # S_BINARY, S_DIMMER, S_SPRINKLER, S_HVAC, S_HEATER. Used for setting/reporting binary (on/off) status. 1=on, 0=off
    #2: "V_LIGHT",	        # \deprecated Same as V_STATUS
    3: "V_PERCENTAGE",	    # S_DIMMER. Used for sending a percentage value 0-100 (%).
    #3: "V_DIMMER",	        # \deprecated Same as V_PERCENTAGE
    4: "V_PRESSURE",	    # S_BARO. Atmospheric Pressure
    5: "V_FORECAST",	    # S_BARO. Whether forecast. string of "stable", "sunny", "cloudy", "unstable", "thunderstorm" or "unknown"
    6: "V_RAIN",	        # S_RAIN. Amount of rain
    7: "V_RAINRATE",	    # S_RAIN. Rate of rain
    8: "V_WIND",	        # S_WIND. Wind speed
    9: "V_GUST",	        # S_WIND. Gust
    10: "V_DIRECTION",	    # S_WIND. Wind direction 0-360 (degrees)
    11: "V_UV",	            # S_UV. UV light level
    12: "V_WEIGHT",	        # S_WEIGHT. Weight(for scales etc)
    13: "V_DISTANCE",	    # S_DISTANCE. Distance
    14: "V_IMPEDANCE",	    # S_MULTIMETER, S_WEIGHT. Impedance value
    15: "V_ARMED",	        # S_DOOR, S_MOTION, S_SMOKE, S_SPRINKLER. Armed status of a security sensor. 1 = Armed, 0 = Bypassed
    16: "V_TRIPPED",	    # S_DOOR, S_MOTION, S_SMOKE, S_SPRINKLER, S_WATER_LEAK, S_SOUND, S_VIBRATION, S_MOISTURE.
    17: "V_WATT",	        # S_POWER, S_BINARY, S_DIMMER, S_RGB_LIGHT, S_RGBW_LIGHT. Watt value for power meters
    18: "V_KWH",	        # S_POWER. Accumulated number of KWH for a power meter
    19: "V_SCENE_ON",	    # S_SCENE_CONTROLLER. Turn on a scene
    20: "V_SCENE_OFF",	    # S_SCENE_CONTROLLER. Turn of a scene
    #21: "V_HVAC_FLOW_STATE",	# S_HEATER, S_HVAC. HVAC flow state ("Off", "HeatOn", "CoolOn", or "AutoChangeOver")
    21: "V_HEATER",	        # \deprecated Same as V_HVAC_FLOW_STATE
    22: "V_HVAC_SPEED",	    # S_HVAC, S_HEATER. HVAC/Heater fan speed ("Min", "Normal", "Max", "Auto")
    23: "V_LIGHT_LEVEL",	# S_LIGHT_LEVEL. Uncalibrated light level. 0-100%. Use V_LEVEL for light level in lux
    24: "V_VAR1",	        # VAR1
    25: "V_VAR2",	        # VAR2
    26: "V_VAR3",	        # VAR3
    27: "V_VAR4",	        # VAR4
    28: "V_VAR5",	        # VAR5
    29: "V_UP",	            # S_COVER. Window covering. Up
    30: "V_DOWN",	        # S_COVER. Window covering. Down
    31: "V_STOP",	        # S_COVER. Window covering. Stop
    32: "V_IR_SEND",	    # S_IR. Send out an IR-command
    33: "V_IR_RECEIVE",	    # S_IR. This message contains a received IR-command
    34: "V_FLOW",	        # S_WATER. Flow of water (in meter)
    35: "V_VOLUME",	        # S_WATER. Water volume
    36: "V_LOCK_STATUS",	# S_LOCK. Set or get lock status. 1=Locked, 0=Unlocked
    37: "V_LEVEL",	        # S_DUST, S_AIR_QUALITY, S_SOUND (dB), S_VIBRATION (hz), S_LIGHT_LEVEL (lux)
    38: "V_VOLTAGE",	    # S_MULTIMETER
    39: "V_CURRENT",	    # S_MULTIMETER
    40: "V_RGB",	        # S_RGB_LIGHT, S_COLOR_SENSOR. Sent as ASCII hex: RRGGBB (RR=red, GG=green, BB=blue component)
    41: "V_RGBW",	        # S_RGBW_LIGHT. Sent as ASCII hex: RRGGBBWW (WW=white component)
    42: "V_ID",	            # Used for sending in sensors hardware ids (i.e. OneWire DS1820b).
    43: "V_UNIT_PREFIX",	# Allows sensors to send in a string representing the unit prefix to be displayed in GUI, not parsed by controller! E.g. cm, m, km, inch.
    44: "V_HVAC_SETPOINT_COOL",	# S_HVAC. HVAC cool setpoint (Integer between 0-100)
    45: "V_HVAC_SETPOINT_HEAT",	# S_HEATER, S_HVAC. HVAC/Heater setpoint (Integer between 0-100)
    46: "V_HVAC_FLOW_MODE",	# S_HVAC. Flow mode for HVAC ("Auto", "ContinuousOn", "PeriodicOn")
    47: "V_TEXT",	        # S_INFO. Text message to display on LCD or controller device
    48: "V_CUSTOM",	        # Custom messages used for controller/inter node specific commands, preferably using S_CUSTOM device type.
    49: "V_POSITION",	    # GPS position and altitude. Payload: latitude;longitude;altitude(m). E.g. "55.722526;13.017972;18"
    50: "V_IR_RECORD",	    # Record IR codes S_IR for playback
    51: "V_PH",	            # S_WATER_QUALITY, water PH
    52: "V_ORP",	        # S_WATER_QUALITY, water ORP : redox potential in mV
    53: "V_EC",	            # S_WATER_QUALITY, water electric conductivity μS/cm (microSiemens/cm)
    54: "V_VAR",	        # S_POWER, Reactive power: volt-ampere reactive (var)
    55: "V_VA",	            # S_POWER, Apparent power: volt-ampere (VA)
    56: "V_POWER_FACTOR",	# S_POWER, Ratio of real power to apparent power: floating point value in the range [-1,..,1]
}

class Internal(IntEnum):
    I_BATTERY_LEVEL = 0	    #!< Battery level
    I_TIME = 1	            #!< Time (request/response)
    I_VERSION = 2	        #!< Version
    I_ID_REQUEST = 3	    #!< ID request
    I_ID_RESPONSE = 4	    #!< ID response
    I_INCLUSION_MODE = 5	#!< Inclusion mode
    I_CONFIG = 6	        #!< Config (request/response)
    I_FIND_PARENT_REQUEST = 7	#!< Find parent
    I_FIND_PARENT_RESPONSE = 8	#!< Find parent response
    I_LOG_MESSAGE = 9	    #!< Log message
    I_CHILDREN = 10	        #!< Children
    I_SKETCH_NAME = 11	    #!< Sketch name
    I_SKETCH_VERSION = 12	#!< Sketch version
    I_REBOOT = 13	        #!< Reboot request
    I_GATEWAY_READY = 14	#!< Gateway ready
    I_SIGNING_PRESENTATION = 15	#!< Provides signing related preferences (first byte is preference version)
    I_NONCE_REQUEST = 16	#!< Request for a nonce
    I_NONCE_RESPONSE = 17	#!< Payload is nonce data
    I_HEARTBEAT_REQUEST = 18	#!< Heartbeat request
    I_PRESENTATION = 19	    #!< Presentation message
    I_DISCOVER_REQUEST = 20	#!< Discover request
    I_DISCOVER_RESPONSE = 21	#!< Discover response
    I_HEARTBEAT_RESPONSE = 22	#!< Heartbeat response
    I_LOCKED = 23	        #!< Node is locked (reason in string-payload)
    I_PING = 24	            #!< Ping sent to node, payload incremental hop counter
    I_PONG = 25	            #!< In return to ping, sent back to sender, payload incremental hop counter
    I_REGISTRATION_REQUEST = 26	#!< Register request to GW
    I_REGISTRATION_RESPONSE = 27	#!< Register response from GW
    I_DEBUG = 28	#!< Debug message
    I_SIGNAL_REPORT_REQUEST = 29	#!< Device signal strength request
    I_SIGNAL_REPORT_REVERSE = 30	#!< Internal
    I_SIGNAL_REPORT_RESPONSE = 31	#!< Device signal strength response (RSSI)
    I_PRE_SLEEP_NOTIFICATION = 32	#!< Message sent before node is going to sleep
    I_POST_SLEEP_NOTIFICATION = 33	#!< Message sent after node woke up (if enabled)


internal_names = {
    0: "I_BATTERY_LEVEL",	# Battery level
    1: "I_TIME",	        # Time (request/response)
    2: "I_VERSION",	        # Version
    3: "I_ID_REQUEST",	    # ID request
    4: "I_ID_RESPONSE",	    # ID response
    5: "I_INCLUSION_MODE",	# Inclusion mode
    6: "I_CONFIG",	        # Config (request/response)
    7: "I_FIND_PARENT_REQUEST",	# Find parent
    8: "I_FIND_PARENT_RESPONSE",	# Find parent response
    9: "I_LOG_MESSAGE",	    # Log message
    10: "I_CHILDREN",	    # Children
    11: "I_SKETCH_NAME",	# Sketch name
    12: "I_SKETCH_VERSION",	# Sketch version
    13: "I_REBOOT",	# Reboot request
    14: "I_GATEWAY_READY",	# Gateway ready
    15: "I_SIGNING_PRESENTATION",	# Provides signing related preferences (first byte is preference version)
    16: "I_NONCE_REQUEST",	# Request for a nonce
    17: "I_NONCE_RESPONSE",	# Payload is nonce data
    18: "I_HEARTBEAT_REQUEST",	# Heartbeat request
    19: "I_PRESENTATION",	# Presentation message
    20: "I_DISCOVER_REQUEST",	# Discover request
    21: "I_DISCOVER_RESPONSE",	# Discover response
    22: "I_HEARTBEAT_RESPONSE",	# Heartbeat response
    23: "I_LOCKED",	        # Node is locked (reason in string-payload)
    24: "I_PING",	        # Ping sent to node, payload incremental hop counter
    25: "I_PONG",	        # In return to ping, sent back to sender, payload incremental hop counter
    26: "I_REGISTRATION_REQUEST",	# Register request to GW
    27: "I_REGISTRATION_RESPONSE",	# Register response from GW
    28: "I_DEBUG",	        # Debug message
    29: "I_SIGNAL_REPORT_REQUEST",	# Device signal strength request
    30: "I_SIGNAL_REPORT_REVERSE",	# Internal
    31: "I_SIGNAL_REPORT_RESPONSE",	# Device signal strength response (RSSI)
    32: "I_PRE_SLEEP_NOTIFICATION",	# Message sent before node is going to sleep
    33: "I_POST_SLEEP_NOTIFICATION",	# Message sent after node woke up (if enabled)
}
