from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from queryset_sequence import QuerySetSequence
from django.db.models import Q
from rest_framework import serializers

from remo_app.remo.api.viewsets import BaseNestedModelViewSet
from remo_app.remo.models import Dataset, Annotation, DatasetImage, ImageFolder, ImageFolderStatistics, AnnotationSet


class BriefUserDatasetFolderSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    dataset_id = serializers.IntegerField(source='dataset.id', read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    preview = serializers.SerializerMethodField()
    total_images = serializers.SerializerMethodField()
    top3_classes = serializers.SerializerMethodField()
    total_classes = serializers.SerializerMethodField()

    class Meta:
        model = ImageFolder
        fields = ('id', 'name', 'dataset_id', 'updated_at', 'created_at', 'preview',
                  'total_images', 'top3_classes', 'total_classes')

    def get_preview(self, instance):
        img = instance.contents.first()
        if img:
            return img.image_object.preview.url if img.image_object.preview else None

        return None

    def get_total_images(self, instance):
        return instance.contents.count()

    def get_top3_classes(self, instance):
        stats = ImageFolderStatistics.objects.filter(image_folder=instance).first()
        if not stats:
            return []
        return stats.statistics.get('top3_classes', [])

    def get_total_classes(self, instance):
        stats = ImageFolderStatistics.objects.filter(image_folder=instance).first()
        if not stats:
            return 0
        return stats.statistics.get('total_classes', 0)


class DatasetImageSerializer(serializers.ModelSerializer):
    view = serializers.SerializerMethodField()
    preview = serializers.SerializerMethodField()
    name = serializers.CharField(source='original_name')
    dimensions = serializers.SerializerMethodField()
    size_in_bytes = serializers.IntegerField(source='image_object.size')
    annotations = serializers.SerializerMethodField()

    class Meta:
        model = DatasetImage
        fields = ('id', 'view', 'preview', 'name', 'annotations', 'dimensions', 'size_in_bytes', 'created_at')

    def get_view(self, instance):
        return instance.view_url()

    def get_preview(self, instance):
        return instance.preview_url()

    def get_dimensions(self, instance):
        return [instance.image_object.width, instance.image_object.height]

    def get_annotations(self, instance):
        all_annotations = []
        indexes = {}
        annotation_sets = AnnotationSet.objects.filter(dataset=instance.dataset)
        for annotation_set in annotation_sets:
            indexes[annotation_set.id] = len(all_annotations)
            all_annotations.append({
                'annotation_set_id': annotation_set.id,
                'coordinates': [],
                'classes': [],
            })


        annotation_sets = Annotation.objects.filter(
            image=instance,
        ).values_list(
            'annotation_set__pk', flat=True
        ).distinct()

        for annotation_set_id in annotation_sets:
            annotations = self.get_annotation_set_annotations(instance, annotation_set_id)
            all_annotations[indexes[annotation_set_id]].update(annotations)

        return all_annotations

    def get_annotation_set_annotations(self, instance, annotation_set_id):
        coordinates = self.get_coordinates(instance, annotation_set_id)
        annotations = {
            'coordinates': [],
            'classes': [],
        }
        if len(coordinates):
            annotations['coordinates'] = coordinates
            return annotations

        annotations['classes'] = self.get_classes(instance, annotation_set_id)
        return annotations

    def get_classes(self, instance, annotation_set_id):
        classes = Annotation.objects.filter(
            image=instance,
            annotation_set__pk=annotation_set_id
        ).values_list(
            'classes__name', flat=True
        ).order_by('classes__name').distinct()

        return list(filter(lambda v: v is not None, list(classes)))

    def get_coordinates(self, instance, annotation_set_id):
        coordinates = Annotation.objects.filter(
            image=instance,
            annotation_set__pk=annotation_set_id
        ).values_list(
            'annotation_objects__coordinates', flat=True
        ).all()

        return list(filter(lambda v: v is not None, list(coordinates)))


class DatasetContentsSerializer(serializers.Serializer):
    record_type = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    folder = serializers.SerializerMethodField()

    def get_record_type(self, instance):
        return self._get_instance_type(instance)

    def get_image(self, instance):
        if self._get_instance_type(instance) != 'image':
            return None

        return DatasetImageSerializer(instance, context=self.context).data

    def get_folder(self, instance):
        if self._get_instance_type(instance) != 'folder':
            return None

        return BriefUserDatasetFolderSerializer(instance, context=self.context).data

    def _get_instance_type(self, instance):
        types = {
            ImageFolder: 'folder',
            DatasetImage: 'image'
        }
        return types.get(type(instance))


class DatasetContents(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      BaseNestedModelViewSet):
    parent_lookup = 'datasets'
    serializer_class = DatasetContentsSerializer

    def get_parent_queryset(self):
        return Dataset.objects.filter(Q(user=self.request.user) | Q(is_public=True))

    def get_contents(self, folder_object=None):
        """
        Return contents of dataset folder
        :param folder_object: folder to list contents of, Default: root
        :return: Response object with paginated results
        """
        folders = ImageFolder.objects.filter(
            dataset=self.parent_pk
        )
        images = DatasetImage.objects.filter(
            dataset=self.parent_pk
        )

        if folder_object:
            images = images.filter(folder=folder_object)
        else:
            images = images.filter(folder__isnull=True)
        folders = folders.filter(parent=folder_object)

        queryset = QuerySetSequence(folders, images)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        return self.get_contents(folder_object=None)

    def retrieve(self, request, *args, **kwargs):
        # TODO: make walk contents/folder1/folder2/..., #333
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        fltr = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_404(ImageFolder, **fltr)
        return self.get_contents(obj)
