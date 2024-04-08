import uno
from com.sun.star.beans import PropertyValue

def create_pie_chart(doc):
    # Get the document's draw pages
    draw_pages = doc.getDrawPages()

    # Create a new draw page
    page = draw_pages.insertNewByIndex(0)

    # Set the title in the center of the page
    title_shape = page.createInstance("com.sun.star.drawing.TextShape")
    title_shape.setString("PROGRESSIVE")
    title_shape.setPosition((2800, 400))
    title_shape.setSize((4000, 500))
    title_shape.setPropertyValue("TextAlign", uno.Enum("com.sun.star.drawing.TextHorizontalAdjust", "CENTER"))
    title_shape.setPropertyValue("TextVerticalAdjust", uno.Enum("com.sun.star.drawing.TextVerticalAdjust", "MIDDLE"))
    page.add(title_shape)

    # Data for the chart
    chart_data = [
        {"label": "1", "icon": "house", "color": 0xFF0000},
        {"label": "2", "icon": "car", "color": 0xFFA500},
        {"label": "3", "icon": "person", "color": 0xFFFF00},
        {"label": "4", "icon": "tree", "color": 0x008000},
        {"label": "5", "icon": "book", "color": 0x0000FF},
        {"label": "6", "icon": "computer", "color": 0x800080},
        {"label": "7", "icon": "phone", "color": 0xFF00FF},
        {"label": "8", "icon": "light_bulb", "color": 0x808080}
    ]

    # Create the pie chart
    chart = page.createInstance("com.sun.star.chart2.PieDiagram")
    chart.setSize((10000, 10000))
    chart.setPosition((500, 2000))
    page.add(chart)

    # Add data points to the chart
    for data_point in chart_data:
        data_row = chart.addNewDataPoint(uno.Enum("com.sun.star.chart2.data.XLabeledDataArray"))
        data_row.addNewPair("Value", float(data_point["label"]))
        data_row.addNewPair("Label", data_point["label"])

    # Customize the chart
    chart.setPropertyValue("ColorScheme", uno.Enum("com.sun.star.chart2.ChartColorScheme", "PRESENTATION"))
    chart.setPropertyValue("ShowDataLabels", True)

    # Add legends for each section
    for i, data_point in enumerate(chart_data):
        legend = chart.createInstance("com.sun.star.chart2.data.LegendEntry")
        legend.setColor(data_point["color"])
        legend.setLabel(data_point["label"])
        chart.setLegend(i, legend)

    # Save the document
    doc.storeAsURL("file:///path/to/your/output/file.odp", ())

def main():
    # Get the UNO component context
    local_context = uno.getComponentContext()

    # Create the service manager
    resolver = local_context.ServiceManager

    # Create a new instance of LibreOffice Impress
    desktop = resolver.createInstanceWithContext("com.sun.star.frame.Desktop", local_context)
    doc = desktop.loadComponentFromURL("private:factory/simpress", "_blank", 0, ())

    # Check if the document was successfully created
    if doc is not None:
        create_pie_chart(doc)
        print("Chart created successfully.")
    else:
        print("Failed to create the document.")

if __name__ == "__main__":
    main()
