from Main_Interface import*
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class Display_angle_output(FigureCanvas):
    def __init__(self, title_angle, width, height, dpi,size):
        # Tạo màn hình vẽ Figure
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#FFFFFF')
        # Thiết lập tên , màu sắc và phông chữ của Figure
        figure.suptitle(title_angle,color='black',fontsize=size)
        # Thiết lập mặt vẽ cho Figure
        self.axes = figure.add_subplot()
        super(Display_angle_output, self).__init__(figure)

    def config_display_output(self,widget,size):
        # nền đồ thị
        widget.axes.set_facecolor('#FFFFFF')
        widget.axes.grid(True)
        # giới hạn trục y
        widget.axes.set_ylim(-50,50)
        # Thiết lập tên các trục tọa độ, màu sắc và phông chữ
        widget.axes.set_xlabel('Time(s)',color='black',fontsize=size)
        widget.axes.set_ylabel('Angle(degree)',color='black',fontsize=size)

class Display_position_output(FigureCanvas):
    def __init__(self, title_angle, width, height, dpi,size):
        # Tạo màn hình vẽ Figure
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#FFFFFF')
        # Thiết lập tên , màu sắc và phông chữ của Figure
        figure.suptitle(title_angle,color='black',fontsize=size)
        # Thiết lập mặt vẽ cho Figure
        self.axes = figure.add_subplot()
        super(Display_position_output, self).__init__(figure)

    def config_display_output(self,widget,size):
        # nền đồ thị
        widget.axes.set_facecolor('#FFFFFF')
        widget.axes.grid(True)
        # giới hạn trục y
        widget.axes.set_ylim(-500,900)
        # Thiết lập tên các trục tọa độ, màu sắc và phông chữ
        widget.axes.set_xlabel('Time(s)',color='black',fontsize=size)
        widget.axes.set_ylabel('Output(mm)',color='black',fontsize=size)

class Display_demension_output(FigureCanvas):
    def __init__(self, title_angle, width, height, dpi,size):
        # Tạo màn hình vẽ Figure
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#FFFFFF')
        # Thiết lập tên , màu sắc và phông chữ của Figure
        figure.suptitle(title_angle,color='black',fontsize=size)
        # Thiết lập mặt vẽ cho Figure
        self.axes = figure.add_subplot()
        super(Display_demension_output, self).__init__(figure)

    def config_display_output(self,widget,size,xlable,ylable):
        # nền đồ thị
        widget.axes.set_facecolor('#FFFFFF')
        widget.axes.grid(True)
        # # giới hạn trục y
        # if(xlable == 'X'):
        #     widget.axes.set_xlim(600,900)
        #     widget.axes.set_ylim(-300,300)
        # elif(ylable == 'X'):
        #     widget.axes.set_ylim(600,900)
        #     widget.axes.set_xlim(-300,300)
        # else:
        #     widget.axes.set_xlim(120,120)
        #     widget.axes.set_ylim(-120,120)
        # Thiết lập tên các trục tọa độ, màu sắc và phông chữ
        widget.axes.set_xlabel(xlable ,color='black',fontsize=size)
        widget.axes.set_ylabel(ylable ,color='black',fontsize=size)

class Display_error(FigureCanvas):
    def __init__(self, title_angle, width, height, dpi,size):
        # Tạo màn hình vẽ Figure
        figure = Figure(figsize=(width,height),dpi=dpi)
        figure.patch.set_facecolor('#FFFFFF')
        # Thiết lập tên , màu sắc và phông chữ của Figure
        figure.suptitle(title_angle,color='black',fontsize=size)
        # Thiết lập mặt vẽ cho Figure
        self.axes = figure.add_subplot()
        super(Display_error, self).__init__(figure)

    def config_display_output(self,widget,size):
        # nền đồ thị
        widget.axes.set_facecolor('#FFFFFF')
        widget.axes.grid(True)
        # giới hạn trục y
        #widget.axes.set_ylim(0,3)
        # Thiết lập tên các trục tọa độ, màu sắc và phông chữ
        widget.axes.set_xlabel('Time(s)',color='black',fontsize=size)
        widget.axes.set_ylabel('Output(mm)',color='black',fontsize=size)

