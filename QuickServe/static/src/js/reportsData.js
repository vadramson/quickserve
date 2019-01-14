

$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/reports/attendance/",
        method:"GET",
        success: function(data){
            console.log('Attendace Here');
            console.log('Attendace Here');
            console.log(data);
            var labels = [];
            var defaultData = [];
            var labels1 = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Date: " + data[i].actDate);
                defaultData.push(data[i].hours);
                labels1.push("Item: " + data[i].item);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Hours",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    },
                    {
                        label: "Quantity",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#graph_bar");

            var barGraph = new Chart(ctx,{
                // type: 'radar',
                // type: 'polarArea',
                type:'bar',
                // type:'doughnut',
                // type:'pie',
                // type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        // position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'My Attendance Statistics '
                    }

                }

            });

        },
        error:function(data){
            console.log("Error Attendance");
            console.log(data);
        }
    });

});


// Purchase Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/reports/purchases/",
        method:"GET",
        success: function(data){
            console.log(data);
            var labels = [];
            var defaultData = [];
            var labels1 = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Product: " + data[i].product_name);
                defaultData.push(data[i].amount);
                labels1.push("Item: " + data[i].item);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Amount",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    },
                    {
                        label: "Quantity",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#purchase");

            var barGraph = new Chart(ctx,{
                // type: 'radar',
                // type: 'polarArea',
                type:'bar',
                // type:'doughnut',
                // type:'pie',
                // type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Magic City Purchase Statistics '
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});


// Buffer Zone

// Cash outflow Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/outflow/cashOut/",
        method:"GET",
        success: function(data){
            console.log(data);
            var labels = [];
            var defaultData = [];
            var labels1 = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Date: " + data[i].dateOp);
                defaultData.push(data[i].amount);
                labels1.push("Quantity: " + data[i].item);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Quantity Loss",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    },
                    {
                        label: "Amount Loss",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#loss");

            var barGraph = new Chart(ctx,{
                type:'bar',
                // type:'doughnut',
                // type:'line',
                //      type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text:  "Magic City's Loss Statistics"
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});

// Products Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/reports/products/",
        method:"GET",
        success: function(data){
            // console.log(data);
            var labels = [];
            var defaultData = [];
            for(var i in data){
                labels.push("Product: " + data[i].namePdt);
                defaultData.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Filter By Quantity only",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    }
                ]
            };


            var ctx = $("#canvas");

            var barGraph = new Chart(ctx,{
                // type:'bar',
                type:'doughnut',
                // type:'line',
                //      type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Products Statistics By Quantity'
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});

// Products Advanced Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/reports/products/",
        method:"GET",
        success: function(data){
            // console.log(data);
            var labels = [];
            var labels1 = [];
            var defaultData = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Product: " + data[i].namePdt);
                defaultData.push(data[i].price);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Filter By Price only: ",

                        backgroundColor: "rgba(38, 185, 154, 0.31)",
                        borderColor: "rgba(38, 185, 154, 0.7)",
                        pointBorderColor: "rgba(38, 185, 154, 0.7)",
                        pointBackgroundColor: "rgba(38, 185, 154, 0.7)",
                        pointHoverBackgroundColor: "#fff",
                        pointHoverBorderColor: "rgba(220,220,220,1)",
                        pointBorderWidth: 1,
                        data:defaultData
                    },
                    {
                        label: "Filter By Quantity ",

                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#Pdtprice");

            var barGraph = new Chart(ctx,{
                type:'bar',
                // type:'doughnut',
                // type:'line',
                // type:'polarArea',
                //      type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Products Statistics By Price'
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});

// Expenses Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/expense/",
        method:"GET",
        success: function(data){
            // console.log(data);
            var labels = [];
            var defaultData = [];
            var labels1 = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Date: " + data[i].dateExp);
                defaultData.push(data[i].amount);
                labels1.push("Quantity: " + data[i].item);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Quantity Loss",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    },
                    {
                        label: "Amount Loss",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#expenses");

            var barGraph = new Chart(ctx,{
                type:'bar',
                type:'doughnut',
                // type:'line',
                //      type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Magic City Expenses Statistics '
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});

// Avaris Graph Function
$(document).ready(function(){
    $.ajax({
        url:"/quickserve/api/avaris/",
        method:"GET",
        success: function(data){
            // console.log(data);
            var labels = [];
            var defaultData = [];
            var labels1 = [];
            var defaultData1 = [];
            for(var i in data){
                labels.push("Date: " + data[i].dateOp);
                defaultData.push(data[i].amount);
                labels1.push("Item: " + data[i].item);
                defaultData1.push(data[i].quantity);
                // console.log(defaultData);
            }

            var randomColorFactor = function() {
                return Math.round(Math.random() * 255);
            };
            var randomColor = function() {
                return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',.7)';
            };

            var chartdata = {
                labels: labels,
                datasets:[
                    {
                        label: "Amount",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData
                    },
                    {
                        label: "Quantity",
                        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850","#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                     backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
//                    borderColor:'rga(200, 200, 200, 0.75)',
                        hoverBackgroundColor:'rgba(220,220,220,0.5)',
                        hoverBorderColor:'rga(200, 200, 200, 1)',
                        borderWidth: 2,
                        borderColor: 'pink',
                        borderSkipped: 'bottom',
                        data:defaultData1
                    }
                ]
            };


            var ctx = $("#avaris");

            var barGraph = new Chart(ctx,{
                // type: 'radar',
                type: 'polarArea',
                // type:'bar',
                // type:'doughnut',
                // type:'pie',
                // type: 'bubble',
                data: chartdata,

                options: {
                    // Elements options apply to all of the options unless overridden in a dataset
                    // In this case, we are setting the border of each bar to be 2px wide and green
                    elements: {
                        rectangle: {
                            borderWidth: 2,
                            backgroundColor: ["#3e95cd", "#26B99A", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
                            borderSkipped: 'bottom'
                        }
                    },
                    responsive: true,
                    legend: {
                        position: 'top'
                    },
                    title: {
                        display: true,
                        text: 'Magic City Avaris Statistics '
                    }

                }

            });

        },
        error:function(data){
            console.log("Error");
            console.log(data);
        }
    });

});