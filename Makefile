all: thermostatCpp

LIBS = libs 

HDRS = $(LIBS)/helper_3d $(LIBS)/I2Cdev.h $(LIBS)/LIBS6050_6Axis_MotionApps20.h $(LIBS)/LIBS6050.h
CMN_OBJS = $(LIBS)/I2Cdev.o $(LIBS)/LIBS6050.o 
DMP_OBJS = SSCLM.o

$(CMN_OBJS) $(DMP_OBJS) $(RAW_OBJS) : $(HDRS)

SSCLM: $(CMN_OBJS) $(DMP_OBJS)
	$(CXX) -o $@ $^ -lm -lpthread -lwiringPi

clean:
	rm -f $(CMN_OBJS) $(DMP_OBJS) $(D3D_OBJS) $(RAW_OBJS)  SSCLM
