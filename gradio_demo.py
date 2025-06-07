import torch
import gradio as gr

model = torch.hub.load('', 'custom', path="runs/train/exp/weights/best.pt", source='local')

title = "基于Gradio的YOLOV5演示项目"
desc = "这是一个基于Gradio的YOLOV5演示项目，非常简洁，非常方便！"

base_conf, base_iou = 0.25, 0.45


def det_image(img, conf, iou):
    model.conf = conf
    model.iou = iou
    return model(img).render()[0]


gr.Interface(inputs=['image', gr.Slider(minimum=0, maximum=1, value=base_conf),
                     gr.Slider(minimum=0, maximum=1, value=base_iou)],
             outputs=["image"],
             fn=det_image,
             title=title,
             live=True,
             description=desc,
             examples=[["../datasets/images/train/20.jpg", base_conf, base_iou], ["../datasets/images/train/80.jpg",
                                                                                  0.45, base_iou]]).launch()

#gr.Image('image', streaming=True)