from uuid import uuid4

from cogment.api.orchestrator_pb2 import (
    TrialStartRequest, TrialFeedbackRequest, TrialActionRequest,
    TrialEndRequest)

from cogment.api.orchestrator_pb2_grpc import TrialStub
from cogment.api.common_pb2 import Action

from cogment.delta_encoding import DecodeObservationData

from cogment.trial import Trial
import grpc

SESSIONS_ID_HEADER_NAME = 'session_id'


class ClientTrial(Trial):
    def __init__(self, conn, trial_start_rep, settings, actor_class,
                 actor_counts, initial_observation, session_id, trial_config):
        super().__init__(trial_start_rep.trial_id, settings, actor_counts, trial_config)
        self.connection = conn
        self.observation = initial_observation
        self.actor_id = trial_start_rep.actor_id
        self.actor_class = actor_class
        self.latest_reward = None
        self.session_id = session_id

    # Perform an action on the trial, and advance time
    def do_action(self, action):
        self.flush_feedback()

        # Send the update to the orchestrator
        update = self.connection.stub.Action(TrialActionRequest(
            trial_id=self.id,
            actor_id=self.actor_id,
            action=Action(content=action.SerializeToString())), metadata=((SESSIONS_ID_HEADER_NAME, self.session_id),))

        self.observation = DecodeObservationData(
            self.actor_class,
            update.observation.data,
            self.observation)

        self.latest_reward = update.reward
        self.tick_id = update.observation.tick_id

        # Return the latest observation
        return self.observation, self.latest_reward

    # Kill the trial
    def end(self):
        if self.plugins:
            # Inform plugins that the trial has ended
            for plugin in self.plugins:
                plugin.trial_ended()
        self.flush_feedback()
        self.connection.stub.End(TrialEndRequest(trial_id=self.id),
                                 metadata=((SESSIONS_ID_HEADER_NAME, self.session_id),))

    def flush_feedback(self):
        feedbacks = list(self._get_all_feedback())

        if feedbacks:
            req = TrialFeedbackRequest(trial_id=self.id)

            req.feedbacks.extend(feedbacks)
            self.connection.stub.GiveFeedback(req, metadata=((SESSIONS_ID_HEADER_NAME, self.session_id),))


class _Connection_impl:
    def __init__(self, stub, settings):
        if not settings:
            raise Exception("missing settings")

        if not stub:
            raise Exception("missing grpc connection stub")

        self.stub = stub
        self.settings = settings

        self.__session_id = str(uuid4())

    def start_trial(self, actor_class, trial_cfg=None, plugins=[]):
        req = TrialStartRequest()

        if trial_cfg:
            req.config.content = trial_cfg.SerializeToString()

        rep = self.stub.Start(req, metadata=((SESSIONS_ID_HEADER_NAME, self.__session_id),))

        observation = DecodeObservationData(
            actor_class, rep.observation.data)

        new_trial = ClientTrial(
            self, rep, self.settings, actor_class, rep.actor_counts,
            observation, self.__session_id, trial_cfg)

        # Start the plugins
        new_trial.plugins = [plugin.start_trial(new_trial) for plugin in plugins]
        return new_trial


class Connection(_Connection_impl):
    def __init__(self, settings, endpoint):
        channel = grpc.insecure_channel(endpoint)
        stub = TrialStub(channel)
        super().__init__(stub, settings)
