def baseline_split(bandwidth_max, camera_indices):
    bandwidth_per_camera = bandwidth_max / len(camera_indices)
    # Assign same bandwidth to all cameras
    output = {camera_idx: bandwidth_per_camera for camera_idx in camera_indices}
    return output


def binary_split(bandwidth_max, camera_indices, bandwidth_optimal, spatial_temporal_model):
    '''
    This assumes the spatial-temporal model knows the current camera c_s and timestep i.
    Basically this could also be implemented as a wrapper where we just give the 
    destination camera as an input
    '''
    # Make sets for relevant and irrelvant cameras based on threshold
    cameras_relevant = set(
        [camera for camera in camera_indices if spatial_temporal_model.thresholded(camera)])
    cameras_irrelevant = set(camera_indices) - cameras_relevant
    # Calculate bandwidths for each set
    bandwidth_cameras_relevant = min(
        bandwidth_max, len(cameras_relevant) * bandwidth_optimal)
    bandwidth_cameras_irrelevant = bandwidth_max - bandwidth_cameras_relevant
    # Assign it to both sets
    output = {camera_idx: bandwidth_cameras_relevant /
              len(cameras_relevant) for camera_idx in cameras_relevant}
    output.update({camera_idx: bandwidth_cameras_irrelevant /
                   len(cameras_irrelevant) for camera_idx in cameras_irrelevant})
    return output


def relative_split(bandwidth_max, camera_indices, spatial_temporal_model):
    # Calculate the combined correlation (multiplication, other variants are also possible)
    sum = 0
    correlations = {}
    for camera_idx in camera_indices:
        correlation = spatial_temporal_model.spatial_correlation(
            camera_idx) * spatial_temporal_model.temporal_correlation(camera_idx)
        sum += correlation
        correlations.update({camera_idx: correlation})
    # Normalize correlation + Multiple by max bandwidth --> Shared percentage
    for key, value in correlations.items():
        correlations[key] = value / sum * bandwidth_max

    return correlations


class FakeSpatialTemporalModel():

    def thresholded(self, camera):
        '''
        Fakes the high-level model of RexCam
        In the correct version this should be calculated by using the different
        correlations
        '''
        return camera == 1 or camera == 8

    def spatial_correlation(self, camera):
        correl = {1: 0.01,
                  4: 0.3,
                  6: 0.95,
                  8: 0.2}
        return correl[camera]

    def temporal_correlation(self, camera):
        correl = {1: 0.05,
                  4: 0.2,
                  6: 0.85,
                  8: 0.6}
        return correl[camera]


if __name__ == "__main__":
    # Data from report 3
    bandwidth_max = 21
    optimal_bandwidth = 9.5
    camera_indices = [1, 4, 6, 8]
    s_t_model = FakeSpatialTemporalModel()

    baseline = baseline_split(bandwidth_max, camera_indices)
    print("Baseline Split:\n{}".format(baseline))

    binary = binary_split(bandwidth_max, camera_indices,
                          optimal_bandwidth, s_t_model)
    print("Binary Split:\n{}".format(binary))

    relative = relative_split(bandwidth_max, camera_indices, s_t_model)
    print("Relative Split:\n{}".format(relative))
